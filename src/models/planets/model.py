from enum import Enum

class SunType(Enum):
    Yellow = 0
    Red = 1
    Blue = 2
    Orange = 3
    Black = 4

class Sun:
    def __init__(self, name: str, sun_type: SunType = SunType.Yellow):
        self.name = name
        self.type = sun_type

class PlanetType(Enum):
    Asteroid = -2
    Moon = -1
    Terrestrial = 0
    Jovian = 1
    Dwarf = 2

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

class TerrestrialMoon(Moon):
    def __init__(self, name: str, parent: TerrestrialPlanet):
        super().__init__(name, parent)

class JovianPlanet(Planet):
    def __init__(self, name: str, moons: list = None):
        super().__init__(
            name,
            PlanetType.Jovian,
            [JovianMoon(moon, self) for moon in moons] if moons is not None else None
        )

class JovianMoon(Moon):
    def __init__(self, name: str, parent: JovianPlanet):
        super().__init__(name, parent)

class Asteroid(Planet):
    def __init__(self, name: str):
        super().__init__(name, PlanetType.Asteroid)

class AsteroidBelt:
    def __init__(self, name, m=1, n=1):
        self.name = name
        self.asteroids = {}
        for i in range(0, m):
            self.asteroids[i] = {}
            for j in range(0, n):
                index = i + j
                self.asteroids[i][j] = Asteroid(f"{name}'s Asteroid #{index}")

class SolarSystem:
    def __init__(self,
                 system_name: str,
                 sun_type: SunType=SunType.Yellow,
                 inner_sector: tuple = None,
                 outer_sector: tuple = None
    ):
        self.sun = Sun(f"{system_name}'s Sun", sun_type)
        self.inner_sector = inner_sector
        self.outer_sector = outer_sector

    def planets(self):
        total_planets = []
        for planet in self.inner_sector:
            if type(planet) is TerrestrialPlanet:
                total_planets.append(planet)
        for planet in self.outer_sector:
            if type(planet) is JovianPlanet:
                total_planets.append(planet)
            elif type(planet) is DwarfPlanet:
                total_planets.append(planet)
        return {f"{planet.name}": planet for planet in total_planets}

    def moons(self):
        total_moons = []
        for planet in self.planets().values():
            for moon in planet.moons:
                total_moons.append(moon)
        return {f"{moon.name}": moon for moon in total_moons}

    def find_planet(self, planet_name):
        planets = self.planets()
        if planet_name not in planets:
            return None
        else:
            found_planet = planets[planet_name]
            return found_planet

    def find_moon(self, moon_name):
        moons = self.moons()
        if moon_name not in moons:
            return None
        else:
            found_moon = moons[moon_name]
            return found_moon

    def asteroid_belts(self, index: int=None):
        valid_belts = (
            self.inner_sector[len(self.inner_sector) - 1],
            self.outer_sector[len(self.outer_sector) - 1]
        )
        if index is None:
            return valid_belts
        else:
            valid_index = index % len(valid_belts)
            return valid_belts[valid_index]

class Sol(SolarSystem):
    def __init__(self):
        super().__init__(
            system_name="Sol",
            sun_type=SunType.Yellow,
            inner_sector=(
                TerrestrialPlanet("Mercury"),
                TerrestrialPlanet("Venus"),
                TerrestrialPlanet("Earth", ["Luna"]),
                TerrestrialPlanet("Mars", ["Phobos", "Deimos"]),
                AsteroidBelt("Ceres")
            ),
            outer_sector=(
                JovianPlanet("Jupiter", ["Europa", "Ganymede", "Callisto"]),
                JovianPlanet("Saturn", ["Titan", "Enceladus"]),
                JovianPlanet("Uranus"),
                JovianPlanet("Neptune", ["Triton"]),
                DwarfPlanet("Pluto"),
                AsteroidBelt("Kuiper")
            )
        )
        self.mercury = self.find_planet("Mercury")
        self.venus = self.find_planet("Venus")
        self.earth = self.find_planet("Earth")
        self.mars = self.find_planet("Mars")
        self.jupiter = self.find_planet("Jupiter")
        self.saturn = self.find_planet("Saturn")
        self.uranus = self.find_planet("Uranus")
        self.neptune = self.find_planet("Neptune")
        self.pluto = self.find_planet("Pluto")


def validate_sol_for_legion(bases: tuple, stations: tuple):
    sol = Sol()
    print(sol.sun.type == SunType.Yellow)

    # Ceres and Kuiper Belt: 2 Star Stations
    print(len(sol.asteroid_belts()) == 2)

    # Dead Planet: TerraStation, StarBase
    print(sol.mercury.name == stations[2])
    print(sol.mercury.name == bases[6])
    print(sol.mercury.type == PlanetType.Terrestrial)
    print(len(sol.venus.moons) == 0)

    # Acid Planet: TerraStation, StarBase
    print(sol.venus.name == stations[1])
    print(sol.venus.name == bases[5])
    print(sol.venus.type == PlanetType.Terrestrial)
    print(len(sol.venus.moons) == 0)

    # Biome Planet: StarBase, TerraStation, LunaBase
    print(sol.earth.name == bases[0])
    print(sol.earth.type == PlanetType.Terrestrial)
    print(sol.earth.name == stations[0])
    print(sol.earth.moons[0].name == bases[1])
    print(sol.earth.moons[0].type == PlanetType.Moon)

    # Barren Planet: 1 StarBase, 2 LunaBases
    print(sol.mars.name == bases[2])
    print(sol.mars.type == PlanetType.Terrestrial)
    print(len(sol.mars.moons) == 2)
    print(sol.mars.moons[0].name == bases[3])
    print(sol.mars.moons[0].type == PlanetType.Moon)
    print(sol.mars.moons[1].name == bases[4])
    print(sol.mars.moons[1].type == PlanetType.Moon)

    # Star Station 1
    ceres_belt = sol.asteroid_belts(0)
    ceres = ceres_belt.asteroids[0][0]
    print(ceres_belt.name == stations[3])
    print(ceres.type == PlanetType.Asteroid)

    # Jovian Station 1
    print(sol.jupiter.name == stations[4])
    print(sol.jupiter.type == PlanetType.Jovian)
    print(len(sol.jupiter.moons) == 3)
    print(sol.jupiter.moons[0].name == bases[7])

    # Jovian Station 2
    print(sol.saturn.name == stations[5])
    print(sol.saturn.type == PlanetType.Jovian)
    print(len(sol.saturn.moons) == 2)
    print(sol.saturn.moons[0].name == bases[8])

    # Jovian Station 3
    print(sol.uranus.name == stations[6])
    print(sol.uranus.type == PlanetType.Jovian)
    print(len(sol.uranus.moons) == 0)

    # Jovian Station 4
    print(sol.neptune.name == stations[7])
    print(sol.neptune.type == PlanetType.Jovian)
    print(len(sol.neptune.moons) == 1)
    print(sol.neptune.moons[0].name == bases[9])

    # Dwarf Station 1
    print(sol.pluto.name == stations[8])
    print(sol.pluto.name == bases[10])
    print(len(sol.pluto.moons) == 0)
    print(sol.pluto.type == PlanetType.Dwarf)

    # Star Station 2
    kuiper_belt = sol.asteroid_belts(1)
    kuiper = kuiper_belt.asteroids[0][0]
    print(kuiper_belt.name == stations[9])
    print(kuiper.type == PlanetType.Asteroid)

    print("All True Validates readiness")

if __name__ == "__main__":
    base_planets = ("Earth", "Mars", "Venus", "Mercury", "Pluto")
    base_moons = ("Luna", "Phobos", "Deimos", "Europa", "Titan", "Triton")
    base_stations = ("Earth", "Venus", "Mercury", "Ceres", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Kuiper")
    validate_sol_for_legion(
        bases=("Earth", "Luna", "Mars", "Phobos", "Deimos", "Venus", "Mercury", "Europa", "Titan", "Triton", "Pluto"),
        stations=("Earth", "Venus", "Mercury", "Ceres", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Kuiper")
    )
