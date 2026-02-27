from aiogram import Dispatcher, F
from aiogram.enums import ChatType

from database import User, Code, OrderCategory, Order, VideoCategory, Video, RecipesCategory, Recipes
from handlers import users, admins
from middlewares import UsersMiddleware


def setup_filters(dispatcher: Dispatcher) -> None:
    dispatcher.update.filter(F.chat.type.in_({ChatType.PRIVATE}))


def setup_middlewares(dp: Dispatcher) -> None:
    dp.update.middleware.register(UsersMiddleware())


def setup_routers(dp: Dispatcher) -> None:
    dp.include_routers(
        users.router,
        admins.router
    )


def setup_tables() -> None:
    User.create_table()
    Code.create_table()
    OrderCategory.create_table()
    Order.create_table()
    VideoCategory.create_table()
    Video.create_table()
    RecipesCategory.create_table()
    Recipes.create_table()
