import requests
import base64
from os import environ


x_folder_id = environ.get('x_folder_id')
api_key = environ.get('api_key')

#Yandex Vision OCR
def encode_file(file_path):
    with open(file_path, "rb") as fid:
        file_content = fid.read()
    return base64.b64encode(file_content).decode("utf-8")


image_path = "C:/?/?/?/?"


resp = requests.post(
    url='https://ocr.api.cloud.yandex.net/ocr/v1/recognizeText',
    headers={
        'Authorization': f'API-KEY {api_key}',
        'x-folder-id': f'{x_folder_id}'
    },
    json={
        "content": encode_file(image_path),
        "mimeType": "image",
        "languageCodes": ["*"],
        "model": "page"
    }
)

answer = resp.json()
print(answer['result']['textAnnotation']['fullText'])

#YandexGPT
msg = 'сделай краткое содержание текста'

text = 'Профессия журналиста складывается из многих составляющих. Немаловажная среди них – работа со словом, ведь именно слово – оружие журналиста, и им, как и любым другим оружием, нужно пользоваться умело. В наши дни, когда средства массовой информации приобрели такое влияние, это особенно актуально. Не случайно лингвисты говорят, что язык СМИ становится моделью общенационального языка – «великого и могучего» . Тем внимательнее пишущая (а также радио– и телевизионная) братия должна относиться к слову, тем грамотнее использовать его богатые возможности.'

resp = requests.post(
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion',
    headers = {
        'Authorization': f'API-KEY {api_key}',
        'x-folder-id': f'{x_folder_id}'
    },
    json = {
        'modelUri': f'gpt://{x_folder_id}/yandexgpt',
        'completionOptions': {
            'stream': False,
            'temperature': 0.6,
            'maxTokens': '1000'
        },
        'messages': [
            {
                'role': 'system',
                'text': msg,
            },
            {
                'role': 'user',
                'text': text,
            }
        ]
    }
)

answer = resp.json()
reply_txt = answer['result']['alternatives'][0]['message']['text']
print(reply_txt)