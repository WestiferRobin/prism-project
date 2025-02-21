from src.utils.enums.planet_enums import PlanetType


class Planet:
    def __init__(self, name: str, planet_type: PlanetType, moons: list = None):
        self.name = name
        self.type = planet_type
        if moons is None:
            moons = []
        self.moons = tuple(moons)

class Moon(Planet):
    def __init__(self, name: str, planet: Planet, moon_type: PlanetType=PlanetType.Moon):
        super().__init__(name, moon_type)
        self.planet = planet

class DwarfPlanet(Planet):
    def __init__(self, name: str):
        super().__init__(name, PlanetType.Dwarf, None)

class TerrestrialPlanet(Planet):
    def __init__(self, name: str, moons: list = None):
        super().__init__(
            name,
            PlanetType.Terrestrial,
            [TerrestrialMoon(moon, self) for moon in moons] if moons is not None else None
        )

class JovianPlanet(Planet):
    def __init__(self, name: str, moons: list = None):
        super().__init__(
            name,
            PlanetType.Jovian,
            [JovianMoon(moon, self) for moon in moons] if moons is not None else None
        )

class TerrestrialMoon(Moon):
    def __init__(self, name: str, parent: TerrestrialPlanet):
        super().__init__(name, parent)

class JovianMoon(Moon):
    def __init__(self, name: str, parent: JovianPlanet):
        super().__init__(name, parent)


