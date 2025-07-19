from src.exceptions import EngineException


class TestException(EngineException):
    def __init__(self, message: str):
        super().__init__(message)

