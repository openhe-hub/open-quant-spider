import redis

from src.redis.RedisUtils import RedisUtils
from src.utils.Configuration import Configuration


def test_export_data():
    redis_utils = RedisUtils(Configuration().config_dict)
    print(redis_utils.export_stock_data())


if __name__ == '__main__':
    test_export_data()
