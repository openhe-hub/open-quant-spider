import requests

from src.model.StockData import StockData


class TencentStockSpider:
    def __init__(self):
        self.data_url = 'https://qt.gtimg.cn/q='
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.105 Safari/537.36'
        }
        self.track: list[str] = []
        self.stock_dict: dict[str, StockData] = {}

    def add_stock(self, stock_id: str):
        self.track.append(stock_id)
        self.stock_dict[stock_id] = StockData(stock_id, '', .0, .0, '')

    def get_once(self):
        resp_dict = {}
        for stock_id in self.track:
            resp = requests.get(f"{self.data_url}{stock_id}", headers=self.headers)
            if resp.text.startswith("v_pv_none_match") or resp.text == "":
                print(f"Err: stock id = {stock_id} not match ")
                resp_dict[stock_id] = ''
            else:
                # print(f"Success: get stock id = {stock_id} once")
                resp_dict[stock_id] = resp.text
        for stock_id in resp_dict.keys():
            self.stock_dict[stock_id] = self.parse(resp_dict[stock_id], stock_id)
            # self.stock_dict[stock_id].report()

    def parse(self, resp_text: str, stock_id: str) -> StockData:
        section = resp_text.split('=')
        header, body = section[0], section[1].split("\"")[1].split("~")
        if header == "" or len(body) == 0:
            print(f"Err: stock id = {stock_id} parse failed.")
            return StockData(stock_id, '', .0, .0, '')
        else:
            # print(f"Success: parse stock id = {stock_id}.")
            return StockData(stock_id, name=body[1], price=body[3], trading_volume=body[6], timestamp=body[30])
