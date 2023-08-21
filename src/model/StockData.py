class StockData:
    def __init__(self, stock_id, name, price, trading_volume, timestamp):
        self.stock_id = stock_id
        self.name = name
        self.price = price
        self.trading_volume = trading_volume
        self.timestamp = timestamp

    def report(self):
        print(f"=====> {self.stock_id} <=====")
        print(f"name = {self.name}")
        print(f"price = {self.price}")
        print(f"trading volume = {self.trading_volume}")
        print(f"timestamp = {self.timestamp}")
        print(f"=====>        <=====")