from datetime import datetime
from random import randint

from pydantic import BaseModel

from src.utils.enums.prism_enums import AgeType
from src.utils.exceptions.date_exceptions import DateException


class Date(BaseModel):
    year: int = 0
    month: int = 0
    day: int = 0
    hour: int = 0
    minute: int = 0
    second: int = 0

    @staticmethod
    def random_date() -> "Date":
        current_date = datetime.now()
        return Date(
            year=randint(current_date.year - AgeType.Ancient.value, 2025),
            month=randint(1, 12),
            day=randint(1, 28),
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


