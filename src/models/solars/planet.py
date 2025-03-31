import uuid

from src.models.solars.model import Solar
from src.models.solars.moon import TerrestrialMoon, JovianMoon
from src.utils.enums.solar_enums import SolarType


class Planet(Solar):
    def __init__(self, name: str, solar_type: SolarType, moons: list = None):
        super().__init__(uuid.uuid4(), name, solar_type)
        self.name = name
        self.type = solar_type
        if moons is None:
            moons = []
        self.moons = tuple(moons)


class DwarfPlanet(Planet):
    def __init__(self, name: str):
        super().__init__(name, SolarType.Dwarf, None)


class TerrestrialPlanet(Planet):
    def __init__(self, name: str, moons: list = None):
        super().__init__(name, SolarType.Terrestrial,
                         [TerrestrialMoon(moon, self) for moon in moons] if moons is not None else None)


class JovianPlanet(Planet):
    def __init__(self, name: str, moons: list = None):
        super().__init__(name, SolarType.Jovian,
                         [JovianMoon(moon, self) for moon in moons] if moons is not None else None)



