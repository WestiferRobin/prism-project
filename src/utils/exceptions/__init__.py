

class PrismException(Exception):
    def __init__(self, message: str, code: int = 500):
        super().__init__(f"{code}: {message}")

class NotFoundException(PrismException):
    def __init__(self, message: str):
        super().__init__(message=message, code=404)

