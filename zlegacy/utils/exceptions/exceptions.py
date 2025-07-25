from src.utils.exceptions import PrismException


class TestException(PrismException):
    def __init__(self, message: str):
        super().__init__(message)

