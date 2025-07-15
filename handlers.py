from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from os import environ, remove
import tempfile
from yandexservices import picture_to_text, text_to_summary_text
from dotenv import load_dotenv


load_dotenv()  # take environment variables

router = Router()
tg_token = environ.get('TG_TOKEN')
bot = Bot(token=tg_token)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать! Для получения краткого содержания отправьте текст или изображение с '
                         'текстом (значок прикрепления -> фото или видео -> выбрать изображение -> сжать изображение)')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Пришлите мне текст или изображение")


@router.message()
async def cmd_message(message: Message):
    if message.text is not None:
        await message.answer(text_to_summary_text(message.text))
    elif message.photo is not None:
        photo = message.photo[-1]
        photo_file = await bot.get_file(photo.file_id)
        tmp_file = tempfile.mktemp(prefix="verfessbot-")
        await bot.download_file(file_path=photo_file.file_path, destination=tmp_file)
        text = picture_to_text(tmp_file)
        remove(tmp_file)
        summary_text = text_to_summary_text(text)
        if len(text)>0:
            await message.answer(text)
        await message.answer(summary_text)
    elif message.document is not None:
        await message.answer('Формат документа не принимается. Отправьте текст или изображение с текстом (значок '
                             'прикрепления -> фото или видео -> выбрать изображение -> сжать изображение)')
