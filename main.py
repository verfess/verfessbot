import asyncio
from aiogram import Bot, Dispatcher
from os import environ

from handlers import router


async def main():
    tg_token = environ.get('TG_TOKEN')
    bot = Bot(token=tg_token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
