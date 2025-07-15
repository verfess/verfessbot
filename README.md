# verfessbot
Testing project for Neimark and HSE

## Проблемы и целевая аудитория 
    
Целевая аудитория: школьники

Проблема: Требуется срочно выучить содержание текста.

## Идеи и сценарии работы бота

Школьник фотографирует необходимый для изучения текст
(разворот учебника), бот представляет краткую выжимку
этого текста, которую можно выучить за минуту.

## Сборка проекта

Требуется python версии >= 3.9

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
```

Создать локальный .env файл и прописать в нем TG_TOKEN, YANDEX_API_KEY, YANDEX_FOLDER_ID

```shell
$ python3 main.py
```