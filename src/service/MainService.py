from threading import Thread

import schedule
import time

from src.model.StockData import StockData
from src.service.DataService import DataService
from src.service.SpiderService import SpiderService
from src.spider.DataSourceManager import DataSourceManager
from src.utils.TimeUtils import TimeUtils


class MainService:
    def __init__(self, config: dict):
        self.spider_service: SpiderService = SpiderService(config)
        self.data_service: DataService = DataService(config)
        self.data_source_manager: DataSourceManager = DataSourceManager(config)
        self.time_utils: TimeUtils = TimeUtils(config)

    def exec_loop(self):
        print("=== OPEN QUANT SPIDER BEGIN RUNNING ===")
        spider_thread = Thread(target=self.spider_service.exec_loop, args=[self.data_source_manager, self.time_utils])
        data_thread = Thread(target=self.data_service.exec_loop, args=[self.data_source_manager, self.time_utils])
        spider_thread.start()
        data_thread.start()
