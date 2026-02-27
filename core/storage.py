from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage


async def setup_storage() -> RedisStorage:
    key_builder = DefaultKeyBuilder(with_bot_id=True, with_destiny=True)
    redis = RedisStorage.from_url('redis://localhost:6379/0', key_builder=key_builder)

    return redis
