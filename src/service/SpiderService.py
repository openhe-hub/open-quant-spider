import time

import schedule

from src.model.StockData import StockData
from schedule import every, repeat

from src.spider.DataSourceManager import DataSourceManager
from src.utils.TimeUtils import TimeUtils, MarketPeriod


class SpiderService:
    def __init__(self, config: dict):
        self.stock_data: dict[str, StockData] = {}

    def run_spider(self, data_source: DataSourceManager):
        self.stock_data = data_source.get()

    def exec_loop(self, data_source: DataSourceManager, time_utils: TimeUtils):
        while True:
            if time_utils.is_market_on():
                self.run_spider(data_source)
                print("get stock data once")
                time.sleep(10)
