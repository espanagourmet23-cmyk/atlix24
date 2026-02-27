import asyncio

from aiogram import Bot, Dispatcher

from core import setup_bot, setup_dispatcher, setup_logging


async def main() -> None:
    setup_logging('INFO')

    bot: Bot = await setup_bot()
    dp: Dispatcher = await setup_dispatcher()

    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
