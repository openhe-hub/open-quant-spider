import time

import schedule

from src.model.StockData import StockData
from schedule import every, repeat

from src.redis.RedisUtils import RedisUtils
from src.spider.DataSourceManager import DataSourceManager


class DataService:
    def __init__(self, config: dict):
        self.stock_data: dict[str, StockData] = {}
        self.redisUtils = RedisUtils(config)

    def run_redis_saver(self, data_source: DataSourceManager):
        for key in data_source.data.keys():
            data_source.data[key].report()
            self.redisUtils.save_stock_data(data_source.data[key])

    def exec_loop(self, data_source: DataSourceManager):
        while True:
            self.run_redis_saver(data_source)
            time.sleep(10)
