from datetime import datetime
from random import randint

from src.utils.exceptions.date_exceptions import DateException

INITIAL_YEAR = 0
MILLENNIUM_YEAR = 2000

NET_TIME = datetime.now()

MIN_SECOND = 0
MAX_SECOND = 59
CURRENT_SECOND = NET_TIME.second

MIN_MINUTE = 0
MAX_MINUTE = 59
CURRENT_MINUTE = NET_TIME.minute

MIN_HOUR = 0
MAX_HOUR = 23
CURRENT_HOUR = NET_TIME.hour

MIN_DAY = 1
MAX_DAY = 7
CURRENT_DAY = (NET_TIME.day % 7) + 1


MIN_WEEK = 1
MAX_WEEK = 4

def current_week():
    current_day = NET_TIME.day

    for week in range(MIN_WEEK, MAX_WEEK):
        min_day = week * MIN_DAY
        max_day = week * MAX_DAY
        if min_day < current_day < max_day:
            return week

    raise DateException(message="WEEK isn't working in constants")

CURRENT_WEEK = current_week()

MIN_MONTH = 1
MAX_MONTH = 4
CURRENT_MONTH = (NET_TIME.month % 4) + 1

MIN_YEAR = INITIAL_YEAR
MAX_YEAR = MILLENNIUM_YEAR
CURRENT_YEAR = NET_TIME.year
EPOCHS = int(CURRENT_YEAR / MILLENNIUM_YEAR)

