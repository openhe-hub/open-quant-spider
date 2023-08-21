from src.utils.Configuration import Configuration
from src.utils.TimeUtils import TimeUtils

if __name__ == '__main__':
    timeUtils = TimeUtils(Configuration().config_dict)
    print(timeUtils.judge_time_session())
