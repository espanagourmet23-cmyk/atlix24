from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .config import config


async def setup_bot() -> Bot:
    default = DefaultBotProperties(parse_mode=ParseMode.HTML, link_preview_is_disabled=True)
    bot = Bot(token=config.bot_token, default=default)

    return bot
