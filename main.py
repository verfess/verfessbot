import asyncio
from aiogram import Bot, Dispatcher
from os import environ
from sys import stderr

from handlers import router


async def main():
    tg_token = environ.get('TG_TOKEN')
    if not tg_token:
        print("ERROR: TG_TOKEN is not set", file=stderr)
        exit(1)
    bot = Bot(token=tg_token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
