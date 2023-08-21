import pymysql

from tests.test import StockData


class MysqlUtils:
    def __init__(self, config: dict):
        mysql_config = config["database"]["mysql"]
        self.host = mysql_config["host"]
        self.port = mysql_config["port"]
        self.user = mysql_config["user"]
        self.password = mysql_config["password"]
        self.db = mysql_config["db"]
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)

    def sync_track_list(self, track_list: list[str]):
        pass

    def sync_stock_data(self, stock_records: dict[str, list[StockData]]):
        pass

    def close(self):
        self.conn.close()


