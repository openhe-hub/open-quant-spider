from redis import ConnectionPool, Redis

from src.model.StockData import StockData


class RedisUtils:
    def __init__(self):
        self.pool = ConnectionPool(host='127.0.0.1', port=6379, db=0)
        self.redis_handler = Redis(connection_pool=self.pool)

    def save_stock_data(self, stock_data: StockData):
        key = f"open-quant-spider:{stock_data.stock_id}:{stock_data.timestamp}"
        value = {
            'stock_id': stock_data.stock_id,
            'name': stock_data.name,
            'price': stock_data.price,
            'trading_volume': stock_data.trading_volume,
            'timestamp': stock_data.timestamp
        }
        self.redis_handler.hmset(key, value)
