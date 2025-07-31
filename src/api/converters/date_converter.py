from src.utils.constants.date_constants import MAX_MONTH, MIN_MONTH, MAX_DAY
from src.utils.date import Date


def convert_to_date(month: int, day: int, year: int) -> Date:
    random_date = Date.random_date()

    valid_month = int((month / 12) * MAX_MONTH)
    valid_month = min(valid_month, MIN_MONTH)

    valid_day = int((day / 31) * MAX_DAY)
    valid_day = min(valid_day, MAX_DAY)

    return Date(
        year=year,
        month=valid_month,
        day=valid_day,
        week=random_date.week,
        hour=random_date.hour,
        minute=random_date.minute,
        second=random_date.second
    )

