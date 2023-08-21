from src.mysql.MysqlUtils import MysqlUtils
from src.utils.Configuration import Configuration


def test_sync_stock(config: dict):
    mysql_utils = MysqlUtils(config)
    mysql_utils.sync_track_list(config["stock"]["track_list"])


if __name__ == '__main__':
    test_sync_stock(Configuration().config_dict)
