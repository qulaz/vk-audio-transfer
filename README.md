# VK audio transfer

Небольшой скрипт для переноса аудиозаписей с одного аккаунта на другой


### Использование

ВАЖНО! Перед началом необходимо зайти в настройки безопасности VK ID 
и отключить там пункт "Защита от подозрительных приложений".

Нужен Python 3 и pip

1. Склонировать репозиторий
2. В папке с репозиторием выполнить
```bash
python -m venv vevn
source venv/bin/activate # Для linux/mac
venv\Scripts\activate.bat # Для windows cmd
venv\Scripts\Activate.ps1 # Для windows powershell

pip install -r requirements.txt

login=88005553535 password=qwerty123 from_user_id=1 python main.py
```

* `login` - номер телефона / email от аккаунта куда переносить аудио
* `password` - пароль от аккаунта куда переносить аудио
* `from_user_id` - ID аккаунта с которого переносить аудио. Аудиозаписи у него должны быть открыты

Теперь можете на полчасика забыть о скрипте и пойти попить чайку. 
Чем больше аудио - тем дольше придется подождать. Аудио переносятся в том же порядке,
что были на исходном аккаунте. Изъятые аудио не переносятся.

### Credits

* https://github.com/vodka2/vkaudiotoken-python - получение токена, способного работать с Audio API
* https://github.com/DedInc/vk_captchasolver - автоматическое решение капч от ВК
* https://github.com/python273/vk_api - удобный враппер над VK API
