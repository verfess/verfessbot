from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Register(StatesGroup):
    name = State()
    age = State()
    number = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main)
    await message.reply('Как дела?')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Вы нажали на кнопку помощи")


@router.message()
async def catalog(message: Message):
    if message.text is not None:
        await message.answer('Эксперимент текст ' + message.text)
    elif message.photo is not None:
        await message.answer('Эксперимент фото ' + str(len(message.photo)))
