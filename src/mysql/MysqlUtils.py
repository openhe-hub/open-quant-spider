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
        # fetch old track list
        cursor = self.conn.cursor()
        sql = "SELECT ticker FROM stocks"
        cursor.execute(sql)
        existing_tickers = {row[0] for row in cursor.fetchall()}
        # find diff set
        new_tickers = set(track_list) - existing_tickers
        # insert new stock
        for ticker in new_tickers:
            sql = "INSERT INTO stocks (ticker) VALUES (%s)"
            cursor.execute(sql, (ticker,))
        # commit & close
        self.conn.commit()
        cursor.close()

    def sync_stock_data(self, stock_records: dict[str, list[StockData]]):
        pass

    def close(self):
        self.conn.close()
