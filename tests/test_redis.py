import redis

from src.mysql.MysqlUtils import MysqlUtils
from src.redis.RedisUtils import RedisUtils
from src.utils.Configuration import Configuration


def test_export_data():
    redis_utils = RedisUtils(Configuration().config_dict)
    mysql_utils = MysqlUtils(Configuration().config_dict)
    records = redis_utils.export_stock_data()
    mysql_utils.sync_stock_data(records)


if __name__ == '__main__':
    test_export_data()
