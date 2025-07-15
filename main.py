import asyncio
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import router, bot


async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
