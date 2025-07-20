

class NexusException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class TestException(NexusException):
    def __init__(self, message: str):
        super().__init__(message)

