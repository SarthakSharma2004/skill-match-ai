from memory.redis_client import get_redis_client



def redis_client_test():
    redis_client = get_redis_client()

    assert redis_client is not None
    assert redis_client.client.ping() == True

    redis_client.client.set("test_key", "test_value")
    assert redis_client.client.get("test_key") == "test_value"

    redis_client.client.delete("test_key")
    assert redis_client.client.get("test_key") is None

    print("Redis client test passed")
    

if __name__ == "__main__":
    redis_client_test()

   
