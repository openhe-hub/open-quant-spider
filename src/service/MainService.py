from threading import Thread

import schedule
import time

from src.model.StockData import StockData
from src.service.DataService import DataService
from src.service.SpiderService import SpiderService
from src.spider.DataSourceManager import DataSourceManager


class MainService:
    def __init__(self, config: dict):
        self.spider_service = SpiderService(config)
        self.data_service = DataService(config)
        self.data_source_manager = DataSourceManager(config)

    def exec_loop(self):
        print("=== OPEN QUANT SPIDER BEGIN RUNNING ===")
        spider_thread = Thread(target=self.spider_service.exec_loop, args=[self.data_source_manager])
        data_thread = Thread(target=self.data_service.exec_loop, args=[self.data_source_manager])
        spider_thread.start()
        data_thread.start()
