import redis

if __name__ == '__main__':
    pool = redis.ConnectionPool(host="127.0.0.1", port=6379)
    redisHandler = redis.Redis(connection_pool=pool)
    redisHandler.set('py-redis', '1')
