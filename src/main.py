from src.service.MainService import MainService
from src.spider.sources.tencent.TencentStockSpider import TencentStockSpider

if __name__ == '__main__':
    main_service = MainService()
    main_service.exec_loop()
