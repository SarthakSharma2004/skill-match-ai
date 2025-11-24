from memory.redis_client import get_redis_client
from core.config import get_settings

settings = get_settings()

redis_client = get_redis_client
redis_client.ping()