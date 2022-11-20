import os
from io import BytesIO

import requests
import vk_api
import vk_captchasolver as vc
from vkaudiotoken import get_vk_official_token


from_user_id = os.environ["from_user_id"]
login = os.environ["login"]
password = os.environ["password"]
official_token = get_vk_official_token(login, password)
token = official_token["token"]
user_agent = official_token["user_agent"]

session = requests.Session()
session.headers.update({"User-Agent": user_agent})


def captcha_handler(captcha):
    res = vc.solve(image=BytesIO(captcha.get_image()))
    print(f"capcha: {captcha.get_url()}; res={res}")
    return captcha.try_again(res)


vk_session = vk_api.VkApi(session=session, api_version="5.181", captcha_handler=captcha_handler)
vk = vk_session.get_api()


def get_audios():
    print("getting audios")

    count = 100
    offset = 0
    audios = []

    while True:
        resp = vk.audio.get(owner_id=from_user_id, count=count, offset=offset)

        if not resp["items"]:
            break

        for audio in resp["items"]:
            audios.append({
                "owner_id": audio["owner_id"],
                "audio_id": audio["id"]
            })

        offset += count
        print(f"Getting audios progress: {offset} / {resp['count']}")

    audios.reverse()
    print("")
    return audios


def transfer_audios(audios: list):
    print("audios transfer started")
    total = len(audios)

    for i, audio in enumerate(audios):
        vk.audio.add(**audio)

        print(f"Audios transfer progress: {i + 1} / {total}")


def main():
    audios = get_audios()
    transfer_audios(audios)

    print("Done!")


if __name__ == "__main__":
    main()
