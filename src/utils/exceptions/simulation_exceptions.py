from src.utils.constants import LAB_VERSION


class VersionException(Exception):
    def __init__(self, version: int, sub_version: int):
        super().__init__(f"Version: {LAB_VERSION}.{version}.{sub_version} doesn't exist. look at main_simulation.py")

class SimulationException(Exception):
    def __init__(self, message: str):
        super().__init__(f"Simulation Error: {message}")

