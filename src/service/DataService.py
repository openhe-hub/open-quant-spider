import time

import schedule

from src.model.StockData import StockData
from schedule import every, repeat

from src.redis.RedisUtils import RedisUtils
from src.spider.DataSourceManager import DataSourceManager
from src.utils.TimeUtils import TimeUtils, MarketPeriod


class DataService:
    def __init__(self, config: dict):
        self.stock_data: dict[str, StockData] = {}
        self.redis_utils: RedisUtils = RedisUtils(config)
        self.enable_sync: bool = config["database"]["auto_sync_on"]
        self.is_sync: bool = False

    def update_sync_status(self, time_utils: TimeUtils):
        if self.is_sync:
            if not time_utils.is_market_on():
                self.is_sync = True
            else:
                self.is_sync = False
        else:
            if not time_utils.is_market_on():
                self.is_sync = False
            else:
                self.is_sync = False

    def run_redis_saver(self, data_source: DataSourceManager):
        for key in data_source.data.keys():
            data_source.data[key].report()
            self.redis_utils.save_stock_data(data_source.data[key])

    def migrate_data(self):
        pass

    def exec_loop(self, data_source: DataSourceManager, time_utils: TimeUtils):
        while True:
            self.update_sync_status(time_utils)
            if time_utils.is_market_on():
                self.run_redis_saver(data_source)
                print("save stock data to redis once")
            elif not self.is_sync:
                print("=== begin migrating data ===")
                self.migrate_data()
                self.is_sync = True

            time.sleep(10)
