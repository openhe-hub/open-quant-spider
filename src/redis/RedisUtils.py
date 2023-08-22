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

    def export_stock_data(self) -> dict[str, list[StockData]]:
        # found cache keys
        pattern = 'open-quant-spider:*'
        cursor = 0
        key_list: list[str] = []
        while True:
            cursor, keys = self.redis_handler.scan(cursor, match=pattern)
            for key in keys:
                key_list.append(key.decode('utf-8'))

            if cursor == 0:
                break
        # query & collect
        res: dict[str, list[StockData]] = {}
        for key in key_list:
            stock_id = key.split(':')[1]
            hash_data = self.redis_handler.hgetall(key)
            hash_data_decoded = {}
            stock_data = StockData('', '', .0, .0, '')
            # decode
            for field, value in hash_data.items():
                hash_data_decoded[field.decode('utf-8')] = value.decode('utf-8')
            # collect
            stock_data.stock_id = hash_data_decoded['stock_id']
            stock_data.name = hash_data_decoded['name']
            stock_data.price = hash_data_decoded['price']
            stock_data.timestamp = hash_data_decoded['timestamp']
            # map
            if stock_id in res.keys():
                res[stock_id].append(stock_data)
            else:
                res[stock_id] = [stock_data]

        return res
