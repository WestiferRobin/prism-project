import uuid

from src.models.drones.model import PrismDrone
from src.models.planets.model import Planet
from src.models.vehicles.ships.star_ships import StarDreadnought, StarCapital, StarFrigate, StarCruiser, StarShip
from src.utils.enums.prism_enums import LegionRank


class LegionFleet:
    def __init__(self, leader_flagship: StarShip = None):
        if leader_flagship is None:
            leader = PrismDrone(rank=LegionRank.Arch)
            leader_flagship = StarCapital(leader)
        self.leader = leader_flagship.lead_officer

        self.ships = (
            leader_flagship,
            StarCapital(LegionRank.Major),
            StarCapital(LegionRank.Captain),

            StarFrigate(LegionRank.Captain),
            StarFrigate(LegionRank.Commander),
            StarFrigate(LegionRank.Lieutenant),

            StarCruiser(LegionRank.Commander),
            StarCruiser(LegionRank.Lieutenant),
            StarCruiser(LegionRank.Lieutenant),
            StarCruiser(LegionRank.Sergeant)
        )

class AdminFleet(LegionFleet):
    def __init__(self, leader: PrismDrone, vice_leader: PrismDrone):
        super().__init__(StarDreadnought(leader, vice_leader))


class LegionArmada:
    def __init__(self, leader:  PrismDrone):
        self.leader = leader
        self.vice_leader = PrismDrone(name=f"{self.leader}'s Vice Admin", rank=LegionRank.Arch)
        self.fleets = {
            self.leader.id: AdminFleet(self.leader, self.vice_leader)
        }

        general_fleet = LegionFleet()
        self.admin_general = general_fleet.leader
        self.fleets[self.admin_general.id] = general_fleet

        admiral_fleet = LegionFleet()
        self.admin_admiral = admiral_fleet.leader
        self.fleets[self.admin_admiral.id] = admiral_fleet

    def find_fleet(self, fleet_id):
        if fleet_id not in self.fleets:
            return None
        fleet = self.fleets[fleet_id]
        return fleet

    def find_ship(self, fleet_id, ship_id):
        fleet = self.find_fleet(fleet_id)
        if fleet is None:
            return None
        if ship_id not in fleet.ships:
            return None
        else:
            return fleet.ships[ship_id]

    def dreadnought(self):
        admin_dreadnought = self.find_ship(self.leader.id, self.vice_leader)
        return admin_dreadnought


class AdminLegion:
    def __init__(self, leader: PrismDrone=None):
        if leader is None:
            leader = PrismDrone(rank=LegionRank.Arch)
        self.name = f"{leader}'s Legion Armada"
        self.legion_armada = LegionArmada(leader)

    def __str__(self):
        return self.name

    def armada(self):
        return self.legion_armada

    def admin(self):
        return self.armada().leader

    def vice(self):
        return self.armada().vice_leader

    def leaders(self):
        return (
            self.admin(),
            self.vice(),
            self.armada().admin_admiral,
            self.armada().admin_general
        )

    def find_leader(self, leader_id):
        for leader in self.leaders():
            if leader.id == leader_id:
                return leader
        return None

    def bases(self):
        bases = []
        for fleet in self.armada().fleets:
            for ship in fleet.ships:
                base = ship.home_base()
                bases.append(base)
        return tuple(bases)

    def planets(self, ignore_moons=False):
        planets = []
        for base in self.bases():
            if base.planet is Planet:
                planets.append(base.planet)
        return tuple(planets)

    def moons(self):
        planets = self.planets(ignore_moons=True)
        moons = []
        for planet in planets:
            for moon in planet.moons:
                moons.append(moon)
        return tuple(moons)

    def dreadnought(self):
        leader_id = self.armada().leader.id
        vice_id = self.armada().vice_leader.id
        return self.armada().find_ship(leader_id, vice_id)

    def citadel(self):
        leader_id = self.armada().leader.id
        citadel = self.armada().find_base(leader_id, 0)
        return citadel

    def find_fleet(self, leader_id):
        return self.armada().find_fleet(leader_id)


if __name__ == "__main__":
    wes = PrismDrone(name="Wes", rank=LegionRank.Arch)
    wes_legion = AdminLegion(wes)

    admin_leader = wes_legion.admin()
    print(admin_leader.name == wes)

    wes_armada = wes_legion.armada()
    print(admin_leader.id == wes_armada.leader.id)

    armada_dreadnought = wes_armada.dreadnought()
    vice_admin = armada_dreadnought.lead_officer
    print(vice_admin.id != admin_leader.id)

    wes_fleet = wes_legion.find_fleet(admin_leader.id)
    print(len(wes_fleet.ships) > 5)
    wes_dreadnought = wes_fleet.ships[0]
    print(armada_dreadnought.id == wes_dreadnought.id)
    print(vice_admin.id == wes_dreadnought.lead_officer.id)

    wes_citadel = wes_legion.citadel()
    citadel_leader = wes_citadel.leader()
    print(admin_leader.id == citadel_leader.id)

