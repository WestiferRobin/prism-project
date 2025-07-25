from src.utils.exceptions import PrismException


class DateException(PrismException):
    def __init__(self, message: str, code: int = 500):
        super().__init__(message, code)

