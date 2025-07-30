from random import randint

from pydantic import BaseModel

import src.utils.constants.date_constants as date_constants
from src.utils.exceptions.date_exceptions import DateException


class Date(BaseModel):
    year: int = date_constants.MIN_YEAR
    month: int = date_constants.MIN_MONTH
    week: int = date_constants.MIN_WEEK
    day: int = date_constants.MIN_DAY
    hour: int = date_constants.MIN_HOUR
    minute: int = date_constants.MIN_MINUTE
    second: int = date_constants.MIN_SECOND

    @staticmethod
    def random_date() -> "Date":
        second = randint(date_constants.MIN_SECOND, date_constants.MAX_SECOND)
        minute = randint(date_constants.MIN_MINUTE, date_constants.MAX_MINUTE)
        hour = randint(date_constants.MIN_HOUR, date_constants.MAX_HOUR)
        day = randint(date_constants.MIN_DAY, date_constants.MAX_DAY)
        week = randint(date_constants.MIN_WEEK, date_constants.MAX_WEEK)
        month = randint(date_constants.MIN_MONTH, date_constants.MAX_MONTH)
        year = randint(date_constants.MIN_YEAR, date_constants.MAX_YEAR)
        return Date(
            year=year,
            month=month,
            week=week,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
        )

    def add(self, tag: str, value: int = 1):
        if tag.lower() == "year":
            self.year += value
        elif tag.lower() == "month":
            self.month += value
        elif tag.lower() == "day":
            self.day += value
        elif tag.lower() == "hour":
            self.hour += value
        elif tag.lower() == "minute":
            self.minute += value
        elif tag.lower() == "second":
            self.second += value
        else:
            raise DateException(f"Unknown date tag: {tag}")


