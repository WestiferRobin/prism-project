from src.utils.constants import LAB_VERSION


class VersionException(Exception):
    def __init__(self, version: int, sub_version: int):
        super().__init__(f"Version: {LAB_VERSION}.{version}.{sub_version} doesn't exist. look at main_simulation.py")


class AtomNotFound(Exception):
    def __init__(self, message):
        super().__init__(f"Atom '{message}' wasn't found in Periodic Table")


