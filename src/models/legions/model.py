from src.models.legions.armada import LegionArmada, AdminArmada
from src.models.prisms.model import PrismDrone
from src.models.ships.star_ships.star_ships import StarShip, StarCruiser, StarFrigate, StarCapital
from src.models.solars.moon import Moon
from src.models.solars.planet import Planet
from src.utils.enums.prism_enums import LegionRank
from src.utils.legion_utils import find_fleet_leaders, find_base_leaders, find_legion_ship, find_legion_base
from src.utils.population_utils import build_legion_population


class Legion:
    def __init__(self, name: str, armada: LegionArmada):
        self.name = name
        self.armada = armada

    def __str__(self):
        return self.name

    def admin(self):
        return self.armada.admin()

    def vice(self):
        return self.armada.vice()

    def leaders(self):
        return self.admin(), self.vice()

    def fleets(self):
        return self.armada.fleets()

    def ships(self):
        return self.armada.ships()

    def ships_by_type(self, ship_type: type):
        if ship_type is StarShip:
            if ship_type is StarCruiser:
                return self.armada.cruiser_ships()
            elif ship_type in StarFrigate:
                return self.armada.frigate_ships()
            elif ship_type in StarCapital:
                return self.armada.capital_ships()
            else:
                return tuple(self.armada.flag_ship())
        return tuple([])

    def bases(self):
        return self.armada.bases()

    def population(self):
        return build_legion_population(self)

    def solar_systems(self):
        solar_systems = {}
        for base in self.bases():
            home_solar = base.home_solar()
            if home_solar.id in solar_systems:
                continue
            solar_systems[home_solar.id] = home_solar
        return tuple(solar_systems.values())

    def planets(self):
        solar_systems = self.solar_systems()
        planets = []
        for solar in solar_systems:
            if solar is not Planet:
                continue
            planets.append(solar)
        return tuple(planets)

    def moons(self):
        solar_systems = self.solar_systems()
        moons = []
        for solar in solar_systems:
            if solar is not Moon:
                continue
            moons.append(solar)
        return tuple(moons)

    def drones(self):
        drones = {}
        if "prisms" not in self.population():
            return None
        drone_population = self.population()["drone"]
        for drone_id in drone_population.keys():
            if drone_id in drones:
                continue
            drones[drone_id] = drone_population[drone_id]
        return tuple(drones.values())


class ArchLegion(Legion):
    def __init__(self, name: str, armada: LegionArmada = None):
        if armada is None:
            armada = LegionArmada()
        super().__init__(name, armada)

    def guardians(self):
        fleet_guardians = find_fleet_leaders(self, self.admin().id, self.vice().id)
        base_guardians = find_base_leaders(self, self.admin().id, self.vice().id)
        all_guardians = (fleet_guardians, base_guardians)
        guardians = {}
        for leader_guardians in all_guardians:
            for guardian in leader_guardians:
                if guardian.id in guardians:
                    continue
                if guardian.rank != LegionRank.Arch:
                    continue
                guardians[guardian.id] = guardian
        return guardians

    def dreadnought(self):
        dreadnought_ship = find_legion_ship(self, self.admin().id, self.vice().id)
        return dreadnought_ship

    def citadel(self):
        citadel = find_legion_base(self, self.admin().id)
        return citadel


class AdminLegion(ArchLegion):
    def __init__(self, name: str, leader: PrismDrone = None):
        armada = AdminArmada(leader)
        self.__admiral = armada.admiral()
        self.__general = armada.general()
        super().__init__(name, armada)

    def admiral(self):
        return self.__admiral

    def general(self):
        return self.__general

    def leaders(self):
        return (
            self.admin(),
            self.vice(),
            self.admiral(),
            self.general()
        )

    def admirals(self):
        admirals = find_fleet_leaders(self, self.admiral().id, self.general().id)
        return admirals

    def generals(self):
        generals = find_base_leaders(self, self.general().id, self.admiral().id)
        return generals
