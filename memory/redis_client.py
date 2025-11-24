from functools import lru_cache
import redis
import os
from core.config import get_settings

settings = get_settings()

class RedisClient:
    '''
    Creates a single reusable Redis connection
    '''

    def __init__(self) :
        redis_url = settings.REDIS_URL

        self.client = redis.from_url(redis_url, decode_responses=True)

        try :
            self.client.ping()
            print("Redis connection successful")

        except Exception as e :
            raise RuntimeError(f"Redis connection failed: {e}")
        
    def set(self, key: int, value: str, ex: int = None):
        return self.client.set(key, value, ex=ex)
    
    def get(self, key: int):
        return self.client.get(key)
    
    def delete(self, key: str):
        return self.client.delete(key)
    
    def exists(self, key: str) -> bool:
        return self.client.exists(key) > 0

        

@lru_cache
def get_redis_client() -> RedisClient:
    return RedisClient()

