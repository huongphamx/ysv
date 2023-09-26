import redis.asyncio as redis_async

from ysv.config import common_settings


redis_aclient = redis_async.from_url(common_settings.REDIS_URL, decode_responses=True)
