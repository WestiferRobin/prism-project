

class PlotException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

try:
    raise PlotException()
except BaseException as ex:
    print(ex)

