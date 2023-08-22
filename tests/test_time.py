from src.utils.Configuration import Configuration
from src.utils.TimeUtils import TimeUtils, MarketPeriod

if __name__ == '__main__':
    timeUtils = TimeUtils(Configuration().config_dict)
    print(timeUtils.get_curr_period())
    print(timeUtils.is_market_on())