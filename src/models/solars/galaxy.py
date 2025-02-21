from src.models.solars.model import Sol, SolarSystem
from src.utils.enums.solar_enums import SunColor


class Galaxy:
    def __init__(self,
        name: str,
        first_quadrant: list=None,
        second_quadrant: list=None,
        third_quadrant: list=None,
        fourth_quadrant: list=None
    ):
        self.name = f"{name} Galaxy"
        self.first_quadrant = [] if first_quadrant is None else first_quadrant
        self.second_quadrant = [] if second_quadrant is None else second_quadrant
        self.third_quadrant = [] if third_quadrant is None else third_quadrant
        self.fourth_quadrant = [] if fourth_quadrant is None else fourth_quadrant

    def solar_systems(self):
        solars = []
        quadrants = (
            self.first_quadrant,
            self.second_quadrant,
            self.third_quadrant,
            self.fourth_quadrant
        )
        for quadrant in quadrants:
            for solar in quadrant:
                solars.append(solar)
        return solars

class MilkywayGalaxy(Galaxy):
    def __init__(self):
        super().__init__(name="Milkyway")
        self.first_quadrant.append(Sol())
        self.second_quadrant.append(SolarSystem("Bov", SunColor.Blue))
        self.third_quadrant.append(SolarSystem("Mol", SunColor.Red))
        self.fourth_quadrant.append(SolarSystem("Sov", SunColor.Yellow))

class AndromedaGalaxy(Galaxy):
    def __init__(self):
        super().__init__(name="Andromeda")
        self.second_quadrant.append(SolarSystem("Mol", SunColor.Yellow))
        self.second_quadrant.append(SolarSystem("Tav", SunColor.Red))
        self.third_quadrant.append(SolarSystem("Jav", SunColor.Blue))
        self.fourth_quadrant.append(SolarSystem("Mov", SunColor.Orange))

class UniverseGalaxy(Galaxy):
    def __init__(self):
        milkyway_galaxy = MilkywayGalaxy()
        andromeda_galaxy = AndromedaGalaxy()
        super().__init__(
            name="Universe",
            first_quadrant=UniverseGalaxy.combine_quadrants(
                source_quadrant=milkyway_galaxy.first_quadrant,
                target_quadrant=andromeda_galaxy.fourth_quadrant
            ),
            second_quadrant=UniverseGalaxy.combine_quadrants(
                source_quadrant=milkyway_galaxy.second_quadrant,
                target_quadrant=andromeda_galaxy.second_quadrant
            ),
            third_quadrant=UniverseGalaxy.combine_quadrants(
                source_quadrant=milkyway_galaxy.fourth_quadrant,
                target_quadrant=andromeda_galaxy.fourth_quadrant
            ),
            fourth_quadrant=UniverseGalaxy.combine_quadrants(
                source_quadrant=andromeda_galaxy.first_quadrant,
                target_quadrant=milkyway_galaxy.fourth_quadrant
            )
        )

    @staticmethod
    def combine_quadrants(source_quadrant, target_quadrant):
        total_quadrant = []
        for sun in source_quadrant:
            total_quadrant.append(sun)
        for sun in target_quadrant:
            total_quadrant.append(sun)
        return total_quadrant