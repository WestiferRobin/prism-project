from src.utils.exceptions import NexusException


class EquationException(NexusException):
    def __init__(self, message):
        super().__init__(message)

