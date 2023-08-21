from src.model.StockData import StockData
from src.spider.sources.tencent.TencentStockSpider import TencentStockSpider


class DataSourceManager:
    def __init__(self, config: dict):
        self.source = config['spider']['default_source']
        self.spider = None
        self.data: dict[str, StockData] = {}
        if self.source == 'tencent':
            self.spider = TencentStockSpider()
            for stock_id in config['stock']['track_list']:
                self.spider.add_stock(stock_id)
        # add more stock spider api

    def config(self):
        pass

    def get(self) -> dict[str, StockData]:
        self.spider.get_once()
        self.data = self.spider.stock_dict
        return self.data
