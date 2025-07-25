from src.utils.exceptions import PrismException


class EquationException(PrismException):
    def __init__(self, message):
        super().__init__(message)

