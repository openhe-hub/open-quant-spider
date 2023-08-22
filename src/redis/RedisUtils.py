from redis import ConnectionPool, Redis

from src.model.StockData import StockData


class RedisUtils:
    def __init__(self, config: dict):
        redis_config = config['database']['redis']
        self.pool = ConnectionPool(host=redis_config['host'], port=redis_config['port'],
                                   db=redis_config['default_database_id'])
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

    def export_stock_data(self, stock_data_list: dict[str, list[StockData]]):
        pass
