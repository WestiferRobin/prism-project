import uuid

from src.models.drones.model import PrismDrone
from src.models.planets.model import Planet, Sol
from src.models.vehicles.ships.star_ships import StarDreadnought, StarCapital, StarFrigate, StarCruiser, StarShip
from src.utils.enums.prism_enums import LegionRank, LEGION_RANKS


class LegionFleet:

    @staticmethod
    def build_capital_ship(ship_type: int):
        ship_index = abs(ship_type) % 3

        lead_officer = PrismDrone(rank=LEGION_RANKS[ship_index])
        vice_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 1])
        tactical_officer = PrismDrone(rank=LEGION_RANKS[3 if ship_index <= 1 else 4])
        science_officer = PrismDrone(rank=LEGION_RANKS[3 if ship_index <= 1 else 4])
        medical_officer = PrismDrone(rank=LEGION_RANKS[3 if ship_index <= 1 else 4])
        engineer_officer = PrismDrone(rank=LEGION_RANKS[3 if ship_index <= 1 else 4])

        ship = StarCapital(
            lead_officer=lead_officer,
            vice_officer=vice_officer,
            tactical_officer=tactical_officer,
            science_officer=science_officer,
            medical_officer=medical_officer,
            engineer_officer=engineer_officer
        )
        return ship

    @staticmethod
    def build_frigate_ship(ship_type: int):
        ship_index = abs(ship_type) % 3

        lead_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 2])
        vice_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 3])
        tactical_officer = PrismDrone(rank=LEGION_RANKS[5])
        science_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])
        medical_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])
        engineer_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])

        ship = StarFrigate(
            lead_officer=lead_officer,
            vice_officer=vice_officer,
            tactical_officer=tactical_officer,
            science_officer=science_officer,
            medical_officer=medical_officer,
            engineer_officer=engineer_officer
        )
        return ship

    @staticmethod
    def build_cruiser_ship(ship_type: int):
        ship_index = abs(ship_type) % 4

        lead_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 2])
        vice_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 3 if ship_index + 3 <= 5 else 5])
        tactical_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index <= 1 else 5])
        science_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])
        medical_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])
        engineer_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])

        ship = StarCruiser(
            lead_officer=lead_officer,
            vice_officer=vice_officer,
            tactical_officer=tactical_officer,
            science_officer=science_officer,
            medical_officer=medical_officer,
            engineer_officer=engineer_officer
        )

        return ship

    def __init__(self, leader_flagship: StarShip = None):
        if leader_flagship is None:
            leader_flagship = LegionFleet.build_capital_ship(0)

        self.leader = leader_flagship.lead_officer

        ships = (
            leader_flagship,
            LegionFleet.build_capital_ship(1),
            LegionFleet.build_capital_ship(2),

            LegionFleet.build_frigate_ship(0),
            LegionFleet.build_frigate_ship(1),
            LegionFleet.build_frigate_ship(2),

            LegionFleet.build_cruiser_ship(0),
            LegionFleet.build_cruiser_ship(1),
            LegionFleet.build_cruiser_ship(2),
            LegionFleet.build_cruiser_ship(3)
        )

        self.ships = { ship.id: ship for ship in ships }

    def find_ship(self, ship_id):
        if ship_id not in self.ships:
            return None
        ship = self.ships[ship_id]
        return ship

    def __ships_by_type(self, ship_type: type):
        ships = []
        for ship in self.ships.values():
            if type(ship) == ship_type:
                ships.append(ship)
        return ships

    def cruiser_ships(self):
        cruiser_ships = self.__ships_by_type(StarCruiser)
        return cruiser_ships

    def frigate_ships(self):
        frigate_ships = self.__ships_by_type(StarFrigate)
        return frigate_ships

    def capital_ships(self):
        capital_ships = self.__ships_by_type(StarCapital)
        return capital_ships

    def flagship(self):
        return self.ships[self.leader.id]

class AdminFleet(LegionFleet):
    def __init__(self, admin_leader: PrismDrone, vice_leader: PrismDrone):
        super().__init__(leader_flagship=StarDreadnought(
                lead_officer=vice_leader,
                vice_officer=PrismDrone(rank=LegionRank.Major),
                tactical_officer=PrismDrone(rank=LegionRank.Major),
                science_officer=PrismDrone(rank=LegionRank.Major),
                medical_officer=PrismDrone(rank=LegionRank.Major),
                engineer_officer=PrismDrone(rank=LegionRank.Major)
            ))
        self.admin_leader = admin_leader

    def dreadnought_ship(self):
        return self.flagship()


class LegionArmada:
    def __init__(self, leader: PrismDrone=None):
        if leader is None:
            leader = PrismDrone(name=f"Admin Leader", rank=LegionRank.Arch)
        self.leader = leader
        self.vice_leader = PrismDrone(name=f"Vice Admin", rank=LegionRank.Arch)
        self.fleets = {
            self.leader.id: AdminFleet(self.leader, self.vice_leader)
        }

        general_fleet = LegionFleet()
        self.admin_general = general_fleet.leader
        self.admin_general.name = f"{self.admin_general.rank.name} Admin General"
        self.fleets[self.admin_general.id] = general_fleet

        admiral_fleet = LegionFleet()
        self.admin_admiral = admiral_fleet.leader
        self.admin_admiral.name = f"{self.admin_admiral.rank.name} Admin Admiral"
        self.fleets[self.admin_admiral.id] = admiral_fleet

    def find_fleet(self, fleet_id):
        if fleet_id not in self.fleets:
            return None
        legion_fleet = self.fleets[fleet_id]
        return legion_fleet

    def find_ship(self, fleet_id, ship_id):
        legion_fleet = self.find_fleet(fleet_id)
        if legion_fleet is None:
            return None
        legion_ship = legion_fleet.find_ship(ship_id)
        return legion_ship

    def cruiser_ship(self, leader_id=None, ship_index: int=0):
        if leader_id is None:
            leader_id = self.leader.id
        if ship_index <= 0:
            ship_index = 0
        arch_fleet = self.find_fleet(leader_id)
        if arch_fleet is None:
            return None
        elif len(arch_fleet.cruiser_ships()) <= 0:
            return None
        fleet_ship = arch_fleet.cruiser_ships()[ship_index]
        return fleet_ship

    def frigate_ship(self, leader_id=None, ship_index: int=0):
        if leader_id is None:
            leader_id = self.leader.id
        if ship_index <= 0:
            ship_index = 0
        arch_fleet = self.find_fleet(leader_id)
        if arch_fleet is None:
            return None
        elif len(arch_fleet.frigate_ships()) <= 0:
            return None
        fleet_ship = arch_fleet.frigate_ships()[ship_index]
        return fleet_ship

    def capital_ship(self, leader_id=None, ship_index: int=0):
        if leader_id is None:
            leader_id = self.leader.id
        if ship_index <= 0:
            ship_index = 0
        arch_fleet = self.find_fleet(leader_id)
        if arch_fleet is None:
            return None
        elif len(arch_fleet.capital_ships()) <= 0:
            return None
        fleet_ship = arch_fleet.capital_ships()[ship_index]
        return fleet_ship

    def admin_ship(self):
        admin_fleet = self.find_fleet(fleet_id=self.leader.id)
        admin_ship = admin_fleet.find_ship(ship_id=self.leader.id)
        return admin_ship

    def vice_ship(self):
        admin_dreadnought = self.find_ship(self.leader.id, self.vice_leader.id)
        return admin_dreadnought

    def armada(self):
        return self.fleets


def get_all_fleet_leaders(fleet_ships):
    fleet_leaders = {}
    for fleet_ship in fleet_ships:
        if fleet_ship.lead_officer.rank.value < LegionRank.Commander.value:
            continue
        fleet_leaders[fleet_ship.lead_officer.id] = fleet_ship.lead_officer
    return tuple(fleet_leaders.values())


class AdminLegion:
    def __init__(self, leader: PrismDrone=None):
        self.legion_armada = LegionArmada(leader)
        self.name = f"{self.legion_armada.leader}'s Legion Armada"

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

    def guardians(self):
        guardian_fleet = self.find_fleet(self.admin().id)
        return get_all_fleet_leaders(guardian_fleet.ships.values())

    def admirals(self):
        admiral_fleet = self.find_fleet(self.admiral().id)
        return get_all_fleet_leaders(admiral_fleet.ships.values())

    def generals(self):
        general_fleet = self.find_fleet(self.general().id)
        return get_all_fleet_leaders(general_fleet.ships.values())

    def guardian(self):
        if len(self.guardians()) == 0:
            return None
        admin_guardian = self.guardians()[0]
        return admin_guardian

    def general(self):
        return self.armada().admin_general

    def admiral(self):
        return self.armada().admin_admiral

def validate_legion_base_cases(admin_legion: AdminLegion):
    admin_leader = admin_legion.admin()
    print("Arch Admin Leader" == f"{admin_leader}")

    armada = admin_legion.armada()
    print(admin_leader.id == armada.leader.id)

    armada_dreadnought = armada.vice_ship()
    vice_admin = armada_dreadnought.lead_officer
    print(vice_admin.id != admin_leader.id)

    fleet = admin_legion.find_fleet(admin_leader.id)
    print(len(fleet.ships) > 5)
    dreadnought = fleet.ships[vice_admin.id]
    print(armada_dreadnought.id == dreadnought.id)
    print(vice_admin.id == dreadnought.lead_officer.id)

    vice_fleet = armada.find_fleet(admin_leader.id)
    print(vice_fleet.leader.id == vice_admin.id)
    print(type(vice_fleet) is AdminFleet)

    vice_dreadnought = vice_fleet.dreadnought_ship()
    vice_arch = vice_dreadnought.lead_officer
    print(vice_arch.id == vice_admin.id)
    print(vice_arch.rank == LegionRank.Arch)
    print(vice_dreadnought.id == vice_dreadnought.id)

    leaders = admin_legion.leaders()
    print("Arch Admin Leader" == leaders[0].name)
    print(leaders[0].id == admin_legion.admin().id)

    print("Arch Vice Admin" == leaders[1].name)
    print(leaders[1].id == admin_legion.vice().id)
    print(leaders[1].id == admin_legion.guardians()[0].id)
    print(admin_legion.guardians()[0].rank == LegionRank.Arch)
    print(admin_legion.guardians()[1].rank == LegionRank.Major)
    print(admin_legion.guardians()[2].rank == LegionRank.Captain)
    print(admin_legion.guardians()[4].rank == LegionRank.Commander)

    print("Arch Admin Admiral" == leaders[2].name)
    print(leaders[2].id == admin_legion.admirals()[0].id)
    print(admin_legion.admirals()[0].rank == LegionRank.Arch)
    print(admin_legion.admirals()[1].rank == LegionRank.Major)
    print(admin_legion.admirals()[2].rank == LegionRank.Captain)
    print(admin_legion.admirals()[4].rank == LegionRank.Commander)

    print("Arch Admin General" == leaders[3].name)
    print(leaders[3].id == admin_legion.generals()[0].id)
    print(admin_legion.generals()[0].rank == LegionRank.Arch)
    print(admin_legion.generals()[1].rank == LegionRank.Major)
    print(admin_legion.generals()[2].rank == LegionRank.Captain)
    print(admin_legion.generals()[4].rank == LegionRank.Commander)

    admin_leader = admin_legion.admin()
    vice_leader = admin_legion.vice()
    admin_general = admin_legion.general()
    admin_admiral = admin_legion.admiral()

    admin_fleet = admin_legion.find_fleet(admin_leader.id)
    print(admin_fleet.admin_leader.id == admin_leader.id)
    print(admin_fleet.leader.id == vice_leader.id)
    print(admin_fleet.dreadnought_ship().lead_officer.id == vice_leader.id)

    general_fleet = admin_legion.find_fleet(admin_general.id)
    print(general_fleet.leader.id == general_fleet.leader.id)
    print(general_fleet.flagship().lead_officer.id == admin_general.id)

    admiral_fleet = admin_legion.find_fleet(admin_admiral.id)
    print(admiral_fleet.leader.id == admiral_fleet.leader.id)
    print(admiral_fleet.flagship().lead_officer.id == admin_admiral.id)

def validate_legion(admin_legion: AdminLegion):
    validate_legion_base_cases(admin_legion)

    population = legion.population()
    print(True if "prisms" in population else False)
    legion_prisms = population["prisms"]
    print(len(legion_prisms) > 0)
    legion_ships = population["ships"]
    print(len(legion_ships) > 0)

    admin_fleet = admin_legion.find_fleet(admin_legion.admin().id)
    admin_flagship = admin_fleet.flagship()
    print(admin_flagship.lead_officer.id == admin_legion.vice().id)
    print(type(admin_flagship) == StarDreadnought)

    admin_leader = admin_legion.admin()
    admin_base = admin_flagship.homebase()
    print(admin_base.id == admin_leader.id)
    print(admin_base.leader.id == admin_leader.id)
    print(admin_base.id == legion.citadel().id)

    admiral_fleet = admin_legion.find_fleet(admin_legion.admiral().id)
    admiral_flagship = admin_fleet.flagship()
    print(admin_legion.admiral().id == admiral_flagship.lead_officer.id)
    admiral_station = admiral_flagship.homebase()

    general_fleet = admin_legion.find_fleet(admin_legion.general().id)
    general_flagship = general_fleet.flagship()
    print(admin_legion.general().id == general_flagship.lead_officer.id)
    general_base = general_flagship.homebase()

    citadel = legion.citadel()
    citadel_leader = citadel.leader()
    print(admin_leader.id == citadel_leader.id)
    print(admin_leader.rank == LegionRank.Arch)

    citadel_planet = citadel.planet()
    print(citadel_planet.is_moon() == False)
    print(len(citadel_planet.orbit()) >= 0)

    citadel_population = citadel.population()
    planet_population = citadel_planet.population()
    has_population = True
    for prism in citadel_population.prisms():
        has_population &= prism.id in planet_population.prisms()
    print("Has population: " + has_population)

    luna_planet = citadel_planet.moon()[0]
    luna_bases = luna_planet.bases()
    luna_base = luna_bases[0]
    print(luna_planet.parent.id == citadel_planet.id)
    print(luna_base.parent.id == citadel.id)
    print(luna_base.leader.rank == LegionRank.Major)

    fleet_ship = citadel_planet.orbit()[2]
    print(fleet_ship.id == legion.dreadnought().id)

def create_child(female: PrismDrone, male: PrismDrone):
    child_dna = str()
    gender_cell_count = 0
    for dna_index in range(len(female.id.hex)):
        female_byte = int(female.id.hex[dna_index], 0xF + 1)
        male_byte = int(male.id.hex[dna_index], 0xF + 1)
        child_byte = hex((female_byte + male_byte) & 0xF)[2:]
        gender_cell_count += 1 if int(child_byte, 0xF + 1) % 2 == 0 else -1
        child_dna += child_byte
    gender = gender_cell_count > 0
    child_id = uuid.UUID(child_dna)
    return PrismDrone(prism_id=child_id, rank=LegionRank.Private, age=0, gender=gender)

if __name__ == "__main__":
    legion = AdminLegion()
    validate_legion(legion)

    print("Figure out for Sol? All ships are on star bases in star system!")
    sol = Sol()

    print("How about visually? Galaxy, Planet, Ship, Base, and Player View Maps?")

    """
    Needs: Planets with ships orbiting
    - Planet is owned by Faction and it's allies
    - Admiral is incharge of routes of ship fleets
    - General is incharge of routes of star bases
    - Vice is incharge of routes of star fleets and bases
    - Admiral is incharge of resources of star armada legion
    
    ex.) Wes is playing as Sergeant Avatar on Star Base
    - Wes starts game with battle with Pirates
    - Wes starts colony on planet
    - Wes becomes Lieutenant of Cruiser
    - Wes is approved by Commander to be Outpost
    - Wes becomes Lieutenant of Frigate
    - Wes becomes Commander of Frigate
    - Wes is approved by Captain to be Town
    - Wes becomes Captain of Frigate
    - Wes is approved by Major to be City
    - Wes becomes Captain of Capital
    - Wes becomes Major of Capital
    - Wes becomes Guardian of Citadel as Arch to be Admin, Vice, Admiral, General 
    """

    """
    Idea: fleets + planets = sol with legion armada
    
    Fleets:
        - AdminFleet:
            - LegionCitadel:
                - Leader: Admin Leader
            - Flagship: LegionDreadnought hovering LegionCitadel
                - Leader: Vice Admin
                - Co-Leader: Vice Major
                - Tactical Leader: Vice Captain
                - Science Leader: Vice Commander
                - Medical Leader: Vice Lieutenant
                - Engineer Leader: Vice Ensign
        - AdmiralFleet:
            - AdmiralStation:
                - Leader: Admiral Admin
            - Flagship: LegionCapital hovering AdmiralStation
                - Leader: Major
                - Co-Leader: Captain
                - Officers: Commanders
        - GeneralFleet:
            - GeneralBase:
                - Leader: General Admin
            - Flagship: LegionCapital hovering GeneralBase
                - Leader: Major
                - Co-Leader: Captain
                - Officers: Commanders
        - GuardianFleet:
            - GuardianStation:
                - Leader: Arch Guardian
            - Flagship: LegionCapital hovering GuardianStation
                - Leader: Major
                - Co-leader: Captain
                - Officers: Commanders
    
    Assume:
        4 leaders but has 3 fleets of Admin, Vice, Admiral, General
        maybe 1 sub leader but has 1 fleet as ViceArch of ViceOrder to become Vice or Admin Leader
        Majors want to be Archs on Base or Citadel or Station
        Captains want to be Majors on Town or City or Station
        Commanders want to be Captains on Town or City or Outpost
        Ensigns to Lieutenants want to be Commanders on Outpost or Town or Station
        Privates to Lances want to be Sergeants to Commanders
    
    sol adds Admin, Vice, Admiral, General
    - Inner:
        - Mercury
        - 
    """
