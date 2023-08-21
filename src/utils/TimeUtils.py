from enum import Enum
from datetime import datetime, time
import time

import requests


class MarketPeriod(Enum):
    PRE_MARKET = 1
    MORNING_TRADE_SESSION = 2
    MORNING_SESSION_CLOSE = 3
    AFTERNOON_TRADE_SESSION = 4
    POST_MARKET = 5
    MARKET_CLOSED = 6
    NULL = 7


class TimePoint:
    def __init__(self, config: dict):
        common_config = config["common"]
        self.morning_begin_time: time = common_config["morning_begin_time"]
        self.morning_end_time: time = common_config["morning_end_time"]
        self.afternoon_begin_time: time = common_config["afternoon_begin_time"]
        self.afternoon_end_time: time = common_config["afternoon_end_time"]


class TimeUtils:
    def __init__(self, config: dict):
        self.time_point = TimePoint(config)
        self.period = MarketPeriod.NULL

    def is_market_on(self) -> bool:
        session = self.get_curr_period()
        return session == MarketPeriod.MORNING_TRADE_SESSION or session == MarketPeriod.AFTERNOON_TRADE_SESSION

    def get_curr_period(self) -> MarketPeriod:
        if self.if_market_off():
            return MarketPeriod.MARKET_CLOSED
        else:
            return self.judge_time_session()

    def judge_time_session(self) -> MarketPeriod:
        now = datetime.now().time()
        if now < self.time_point.morning_begin_time:
            return MarketPeriod.PRE_MARKET
        elif self.time_point.morning_begin_time <= now <= self.time_point.morning_end_time:
            return MarketPeriod.MORNING_TRADE_SESSION
        elif self.time_point.morning_end_time < now < self.time_point.afternoon_begin_time:
            return MarketPeriod.MORNING_SESSION_CLOSE
        elif self.time_point.afternoon_begin_time <= now <= self.time_point.afternoon_end_time:
            return MarketPeriod.AFTERNOON_TRADE_SESSION
        elif now > self.time_point.afternoon_end_time:
            return MarketPeriod.POST_MARKET
        else:
            print(f"Err: cannot judge market session, time = {now.strftime('%Y-%m-%d %H:%M:%S')}")
            return MarketPeriod.NULL

    def if_market_off(self) -> bool:
        today = datetime.now().strftime('%Y%m%d')
        holiday_api = f"http://api.goseek.cn/Tools/holiday?date={today}"
        resp = requests.get(holiday_api)
        json_data = resp.json()
        is_holiday = json_data["data"] in [1, 2]
        if is_holiday == 0:  # workday && Mon ~ Fri
            return datetime.now().weekday() < 5
        elif is_holiday == 1:  # holiday
            return False
        else:
            print(f"Err: cannot judge market status, data = {json_data}")
            return False
