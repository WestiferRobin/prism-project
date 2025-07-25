

class PrismException(Exception):
    def __init__(self, message: str, code: int):
        super().__init__(f"{code}: {message}")
