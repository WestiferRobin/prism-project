from src.models.legions.armada import LegionArmada, AdminArmada
from src.models.drones.prism import PrismDrone
from src.models.legions.legionfleet import LegionFleet, AdminFleet
from src.models.planets.planet import Planet, Moon
from src.models.planets.solar_system import Sol
from src.models.ships.star_ships import StarCruiser, StarFrigate, StarCapital, StarShip
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
        if not ship_type is StarShip:
            return tuple([])
        if ship_type is StarCruiser:
            return self.armada.cruiser_ships()
        elif ship_type in StarFrigate:
            return self.armada.frigate_ships()
        elif ship_type in StarCapital:
            return self.armada.capital_ships()
        else:
            return tuple(self.armada.flag_ship())

    def bases(self):
        return self.armada.bases()

    def population(self):
        return build_legion_population(self)

    def solars(self):
        solars = {}
        for base in self.bases():
            home_solar = base.home_solar()
            if home_solar.id in solars:
               continue
            solars[home_solar.id] = home_solar
        return tuple(solars.values())

    def planets(self):
        solars = self.solars()
        planets = []
        for solar in solars:
            if solar is not Planet:
                continue
            planets.append(solar)
        return tuple(planets)

    def moons(self):
        solars = self.solars()
        moons = []
        for solar in solars:
            if solar is not Moon:
                continue
            moons.append(solar)
        return tuple(moons)

    def drones(self):
        drones = {}
        if "drones" not in self.population():
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
    def __init__(self, name: str, leader: PrismDrone=None):
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


def validate_legion_base_cases(admin_legion: AdminLegion):
    admin_leader = admin_legion.admin()
    print("Arch Admin Leader" == f"{admin_leader}")

    armada = admin_legion.armada()
    print(admin_leader.id == armada.__admin.id)

    armada_dreadnought = armada.vice_ship()
    vice_admin = armada_dreadnought.lead_officer
    print(vice_admin.id != admin_leader.id)

    fleet = admin_legion.find_fleet(admin_leader.id)
    print(len(fleet.ships) > 5)
    dreadnought = fleet.ships[vice_admin.id]
    print(armada_dreadnought.id == dreadnought.id)
    print(vice_admin.id == dreadnought.lead_officer.id)

    vice_fleet = armada.find_armada_fleet(admin_leader.id, )
    print(vice_fleet.__admin.id == vice_admin.id)
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
    print(admin_fleet.__admin.id == admin_leader.id)
    print(admin_fleet.fleet_leader.id == vice_leader.id)
    print(admin_fleet.dreadnought_ship().lead_officer.id == vice_leader.id)

    general_fleet = admin_legion.find_fleet(admin_general.id)
    print(general_fleet.fleet_leader.id == general_fleet.fleet_leader.id)
    print(general_fleet.flag_ship().lead_officer.id == admin_general.id)

    admiral_fleet = admin_legion.find_fleet(admin_admiral.id)
    print(admiral_fleet.fleet_leader.id == admiral_fleet.fleet_leader.id)
    print(admiral_fleet.flag_ship().lead_officer.id == admin_admiral.id)

def validate_legion(admin_legion: AdminLegion):
    validate_legion_base_cases(admin_legion)

    population = legion.population()
    print(True if "prisms" in population else False)
    legion_prisms = population["prisms"]
    print(len(legion_prisms) > 0)
    legion_ships = population["ships"]
    print(len(legion_ships) > 0)

    admin_fleet = admin_legion.find_fleet(admin_legion.admin().id)
    admin_flagship = admin_fleet.flag_ship()
    print(admin_flagship.lead_officer.id == admin_legion.vice().id)
    print(type(admin_flagship) == StarDreadnought)

    admin_leader = admin_legion.admin()
    admin_base = admin_flagship.homebase()
    print(admin_base.id == admin_leader.id)
    print(admin_base.__admin.id == admin_leader.id)
    print(admin_base.id == legion.citadel().id)

    admiral_fleet = admin_legion.find_fleet(admin_legion.admiral().id)
    admiral_flagship = admin_fleet.flag_ship()
    print(admin_legion.admiral().id == admiral_flagship.lead_officer.id)
    admiral_station = admiral_flagship.homebase()

    general_fleet = admin_legion.find_fleet(admin_legion.general().id)
    general_flagship = general_fleet.flag_ship()
    print(admin_legion.general().id == general_flagship.lead_officer.id)
    general_base = general_flagship.homebase()

    citadel = legion.citadel()
    citadel_leader = citadel.__admin()
    print(admin_leader.id == citadel_leader.id)
    print(admin_leader.rank == LegionRank.Arch)

    citadel_planet = citadel.planet()
    print(citadel_planet.is_moon() == False)
    print(len(citadel_planet.orbit()) >= 0)

    citadel_population = citadel.population()
    planet_population = citadel_planet.population()
    has_population = True
    for prism in citadel_population.drones():
        has_population &= prism.id in planet_population.drones()
    print("Has population: " + has_population)

    luna_planet = citadel_planet.moon()[0]
    luna_bases = luna_planet.bases()
    luna_base = luna_bases[0]
    print(luna_planet.parent.id == citadel_planet.id)
    print(luna_base.parent.id == citadel.id)
    print(luna_base.__admin.rank == LegionRank.Major)

    fleet_ship = citadel_planet.orbit()[2]
    print(fleet_ship.id == legion.dreadnought().id)

if __name__ == "__main__":
    legion = AdminLegion()
    validate_legion(legion)

    print("Figure out for Sol? All ships are on star bases in star system!")
    sol = Sol()

    print("How about visually? Galaxy, Planet, LegionShip, Base, and Player View Maps?")

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
    - Wes can destroy Admin and ally with Emperor
    - Wes can ally with Fett and Hutt Exchange to defeat Emperor
    - Wes can fight with Fett Ascendancy, Hutt Remnant, Imperial Remnant, Emperor Home-worlds
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
                - Co-__admin: Captain
                - Officers: Commanders
    
    Assume:
        4 leaders but has 3 fleets of Admin, Vice, Admiral, General
        maybe 1 sub __admin but has 1 fleet as ViceArch of ViceOrder to become Vice or Admin Leader
        Majors want to be Archs on Base or Citadel or Station
        Captains want to be Majors on Town or City or Station
        Commanders want to be Captains on Town or City or Outpost
        Ensigns to Lieutenants want to be Commanders on Outpost or Town or Station
        Privates to Lances want to be Sergeants to Commanders
    
    """
