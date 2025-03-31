import uuid

from src.models.solars.model import Solar
from src.utils.enums.solar_enums import SolarType


class Moon(Solar):
    def __init__(self, name: str, planet):
        super().__init__(uuid.uuid4(), name, SolarType.Moon)
        self.planet = planet


class TerrestrialMoon(Moon):
    def __init__(self, name: str, parent):
        super().__init__(name, parent)


class JovianMoon(Moon):
    def __init__(self, name: str, parent):
        super().__init__(name, parent)

