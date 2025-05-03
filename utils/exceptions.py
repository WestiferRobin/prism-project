

class VersionException(Exception):
    def __init__(self, version: int, sub_version: int):
        super().__init__(f"Version: {version}.{sub_version} doesn't exist. look at main_simulation.py")


class PlotException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


