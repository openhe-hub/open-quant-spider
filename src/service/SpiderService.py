import time

import schedule

from src.model.StockData import StockData
from schedule import every, repeat

from src.spider.DataSourceManager import DataSourceManager


class SpiderService:
    def __init__(self):
        self.stock_data: dict[str, StockData] = {}

    def run_spider(self, data_source: DataSourceManager):
        self.stock_data = data_source.get()

    def exec_loop(self, data_source: DataSourceManager):
        while True:
            self.run_spider(data_source)
            time.sleep(10)
