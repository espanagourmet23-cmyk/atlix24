from aiogram import Dispatcher

from .storage import setup_storage
from .setup import setup_filters, setup_middlewares, setup_routers, setup_tables


async def setup_dispatcher() -> Dispatcher:
    storage = await setup_storage()
    dp = Dispatcher(storage=storage)
    dp.startup.register(setup_tables)

    setup_filters(dp)
    setup_middlewares(dp)
    setup_routers(dp)

    return dp
