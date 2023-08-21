from src.service.MainService import MainService
from src.spider.sources.tencent.TencentStockSpider import TencentStockSpider
from src.utils.Configuration import Configuration

if __name__ == '__main__':
    config = Configuration()
    main_service = MainService(config.config_dict)
    main_service.exec_loop()
