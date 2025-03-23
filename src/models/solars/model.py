import random
import uuid

from src.models.solars.asteroid import AsteroidBelt
from src.models.solars.planet import TerrestrialPlanet, JovianPlanet, DwarfPlanet
from src.models.solars.sun import Sun
from src.utils.enums.solar_enums import SunColor, SolarType
from src.utils.solar_utils import find_terrestrial_count, find_jovian_count, find_dwarf_count


class Solar:
    def __init__(self,
        solar_id,
        name: str,
        solar_type: SolarType
    ):
        self.id = solar_id
        self.name = name
        self.type = solar_type


class SolarSystem:
    def __init__(self,
        system_name: str,
        sun_color: SunColor=SunColor.Yellow,
        system_id=None,
        inner_sector: tuple = None,
        outer_sector: tuple = None
    ):
        if system_id is None:
            system_id = uuid.uuid4()
        self.id = system_id
        self.sun = Sun(self.id, f"{system_name}'s Sun", sun_color)

        raw_count = 0
        for hex_byte in self.id.hex:
            system_byte = int(hex_byte, 16)
            if system_byte % 2 == 0:
                raw_count += 1
            elif system_byte % 3 == 0:
                raw_count -= 1

        if inner_sector is None or outer_sector is None:
            terrestrial_count = find_terrestrial_count(sun_color)
            jovian_count = find_jovian_count(sun_color)
            dwarf_count = find_dwarf_count(sun_color)
            if inner_sector is None:
                inner_moons_options = (0, 0, 1, 2)
                chosen_options = set()

                sector = []
                for terrestrial_id in range(terrestrial_count):
                    option_index = random.choice([i for i in range(0, 4)])
                    while option_index in chosen_options and len(chosen_options) < 4:
                        option_index = random.choice([i for i in range(0, 4)])
                    inner_moon_size = inner_moons_options[option_index]
                    planet = TerrestrialPlanet(
                        name=f"Terrestrial Planet #{terrestrial_id}",
                        moons=[f"Terrestrial Moon #{moon_id}" for moon_id in range(inner_moon_size)],
                    )
                    sector.append(planet)
                    chosen_options.add(option_index)

                sector.append(AsteroidBelt(f"{system_name}'s Inner Belt"))
                inner_sector = tuple(sector)
            if outer_sector is None:
                outer_moons_options = (3, 2, 0, 1)
                chosen_options = set()

                sector = []
                for jovian_id in range(jovian_count):
                    option_index = random.choice([i for i in range(0, 4)])
                    while option_index in chosen_options and len(chosen_options) < 4:
                        option_index = random.choice([i for i in range(0, 4)])
                    inner_moon_size = outer_moons_options[option_index]
                    planet = JovianPlanet(
                        name=f"Jovian Planet #{jovian_id}",
                        moons=[f"Jovian Moon #{moon_id}" for moon_id in range(inner_moon_size)],
                    )
                    sector.append(planet)
                    chosen_options.add(option_index)

                for dwarf_id in range(dwarf_count):
                    planet = DwarfPlanet(name=f"Jovian Planet #{dwarf_id}")
                    sector.append(planet)

                sector.append(AsteroidBelt(f"{system_name}'s Outer Belt"))
                outer_sector = tuple(sector)

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
        super().__init__(system_name="Sol", sun_color=SunColor.Yellow, inner_sector=(
            TerrestrialPlanet("Mercury"),
            TerrestrialPlanet("Venus"),
            TerrestrialPlanet("Earth", ["Luna"]),
            TerrestrialPlanet("Mars", ["Phobos", "Deimos"]),
            AsteroidBelt("Ceres")
        ), outer_sector=(
            JovianPlanet("Jupiter", ["Europa", "Ganymede", "Callisto"]),
            JovianPlanet("Saturn", ["Titan", "Enceladus"]),
            JovianPlanet("Uranus"),
            JovianPlanet("Neptune", ["Triton"]),
            DwarfPlanet("Pluto"),
            AsteroidBelt("Kuiper")
        ))
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
    print(sol.sun.type == SunColor.Yellow)

    # Ceres and Kuiper Belt: 2 Star Stations
    print(len(sol.asteroid_belts()) == 2)

    # Dead Planet: TerraStation, StarBase
    print(sol.mercury.name == stations[2])
    print(sol.mercury.name == bases[6])
    print(sol.mercury.type == SolarType.Terrestrial)
    print(len(sol.venus.moons) == 0)

    # Acid Planet: TerraStation, StarBase
    print(sol.venus.name == stations[1])
    print(sol.venus.name == bases[5])
    print(sol.venus.type == SolarType.Terrestrial)
    print(len(sol.venus.moons) == 0)

    # Biome Planet: StarBase, TerraStation, LunaBase
    print(sol.earth.name == bases[0])
    print(sol.earth.type == SolarType.Terrestrial)
    print(sol.earth.name == stations[0])
    print(sol.earth.moons[0].name == bases[1])
    print(sol.earth.moons[0].type == SolarType.Moon)

    # Barren Planet: 1 StarBase, 2 LunaBases
    print(sol.mars.name == bases[2])
    print(sol.mars.type == SolarType.Terrestrial)
    print(len(sol.mars.moons) == 2)
    print(sol.mars.moons[0].name == bases[3])
    print(sol.mars.moons[0].type == SolarType.Moon)
    print(sol.mars.moons[1].name == bases[4])
    print(sol.mars.moons[1].type == SolarType.Moon)

    # Star Station 1
    ceres_belt = sol.asteroid_belts(0)
    ceres = ceres_belt.asteroids[0][0]
    print(ceres_belt.name == stations[3])
    print(ceres.type == SolarType.Asteroid)

    # Jovian Station 1
    print(sol.jupiter.name == stations[4])
    print(sol.jupiter.type == SolarType.Jovian)
    print(len(sol.jupiter.moons) == 3)
    print(sol.jupiter.moons[0].name == bases[7])

    # Jovian Station 2
    print(sol.saturn.name == stations[5])
    print(sol.saturn.type == SolarType.Jovian)
    print(len(sol.saturn.moons) == 2)
    print(sol.saturn.moons[0].name == bases[8])

    # Jovian Station 3
    print(sol.uranus.name == stations[6])
    print(sol.uranus.type == SolarType.Jovian)
    print(len(sol.uranus.moons) == 0)

    # Jovian Station 4
    print(sol.neptune.name == stations[7])
    print(sol.neptune.type == SolarType.Jovian)
    print(len(sol.neptune.moons) == 1)
    print(sol.neptune.moons[0].name == bases[9])

    # Dwarf Station 1
    print(sol.pluto.name == stations[8])
    print(sol.pluto.name == bases[10])
    print(len(sol.pluto.moons) == 0)
    print(sol.pluto.type == SolarType.Dwarf)

    # Star Station 2
    kuiper_belt = sol.asteroid_belts(1)
    kuiper = kuiper_belt.asteroids[0][0]
    print(kuiper_belt.name == stations[9])
    print(kuiper.type == SolarType.Asteroid)

    print("All True Validates readiness")

if __name__ == "__main__":
    base_planets = ("Earth", "Mars", "Venus", "Mercury", "Pluto")
    base_moons = ("Luna", "Phobos", "Deimos", "Europa", "Titan", "Triton")
    base_stations = ("Earth", "Venus", "Mercury", "Ceres", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Kuiper")
    validate_sol_for_legion(
        bases=("Earth", "Luna", "Mars", "Phobos", "Deimos", "Venus", "Mercury", "Europa", "Titan", "Triton", "Pluto"),
        stations=("Earth", "Venus", "Mercury", "Ceres", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Kuiper")
    )