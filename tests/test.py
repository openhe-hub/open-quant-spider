# -*- coding: utf-8 -*-
import requests

data_url = 'https://qt.gtimg.cn/q='
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/84.0.4147.105 Safari/537.36'
}


class StockData:
    def __init__(self, stock_id, name, price, trading_volume):
        self.stock_id = stock_id
        self.name = name
        self.price = price
        self.trading_volume = trading_volume

    def report(self):
        print(f"=====> {self.stock_id} <=====")
        print(f"name = {self.name}")
        print(f"price = {self.price}")
        print(f"trading volume = {self.trading_volume}")
        print(f"=====>        <=====")


def parse(resp_str: str) -> StockData:
    section = resp_str.split('=')
    header, body = section[0], section[1].split("\"")[1].split("~")
    print(header, body)
    return StockData(body[2], body[1], body[3], body[6])


if __name__ == '__main__':
    # stock_id = input("please input the stock code")
    resp = requests.get(f"{data_url}sh601003", headers=headers)
    resp_str = resp.text
    print(resp_str)
    stock_data = parse(resp_str)
    stock_data.report()
