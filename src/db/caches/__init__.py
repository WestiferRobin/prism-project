import redis.asyncio as redis
from src.db import settings


def get_redis():
    return redis.from_url(settings.cache_url, decode_responses=True)

