from src.utils.exceptions import NexusException


class TestException(NexusException):
    def __init__(self, message: str):
        super().__init__(message)

