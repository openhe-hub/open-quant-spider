from src.model.StockData import StockData
from src.spider.sources.tencent.TencentStockSpider import TencentStockSpider


class DataSourceManager:
    def __init__(self, source: str):
        self.source = source
        self.spider = None
        self.data: dict[str, StockData] = {}
        if source == 'tencent':
            self.spider = TencentStockSpider()
            self.spider.add_stock("sh601002")
        # add more stock spider api

    def config(self):
        pass

    def get(self) -> dict[str, StockData]:
        self.spider.get_once()
        self.data = self.spider.stock_dict
        return self.data
