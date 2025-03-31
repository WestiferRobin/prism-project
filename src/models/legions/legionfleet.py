from src.models.prisms.model import PrismDrone
from src.models.ships.star_ships.star_ships import StarCapital, StarFrigate, StarCruiser, StarShip, StarDreadnought
from src.utils.enums.prism_enums import LEGION_RANKS, LegionRank
from src.utils.fleet_utils import find_fleet_ships_by_type


class LegionFleet:
    """
    total is 20 prisms

    ex.) StarCapital has 20 prisms
    bridge-crew:
    - __admin: Captain
    - vice: Commander
    - tactical: Lieutenant
    - science: Lieutenant
    - medical: Lieutenant
    - engineer: Lieutenant
    standard-crew:
    - 1 Sergeant
    - 2 Ensign
    - 3 Lance
    - 4 Corporal
    - 4 Private

    """
    @staticmethod
    def build_capital_ship(ship_type: int):
        ship_index = abs(ship_type) % 3

        lead_officer = PrismDrone(rank=LEGION_RANKS[ship_index])
        vice_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 1])
        tactical_officer = PrismDrone(rank=LEGION_RANKS[3 if ship_index <= 1 else 4])
        science_officer = PrismDrone(rank=LEGION_RANKS[3 if ship_index <= 1 else 4])
        medical_officer = PrismDrone(rank=LEGION_RANKS[3 if ship_index <= 1 else 4])
        engineer_officer = PrismDrone(rank=LEGION_RANKS[3 if ship_index <= 1 else 4])

        crew = list()
        ranks = {
            1: [LegionRank.Sergeant],
            2: [LegionRank.Ensign],
            3: [LegionRank.Lance],
            4: [LegionRank.Corporal, LegionRank.Private]
        }
        for times in ranks.keys():
            crew_ranks = ranks[times]
            for _ in range(times):
                for crew_rank in crew_ranks:
                    crew_member = PrismDrone(rank=crew_rank)
                    crew.append(crew_member)

        ship = StarCapital(
            lead_officer=lead_officer,
            vice_officer=vice_officer,
            tactical_officer=tactical_officer,
            science_officer=science_officer,
            medical_officer=medical_officer,
            engineer_officer=engineer_officer,
            crew=crew
        )
        return ship

    """
    total is 16 prisms

    ex.) StarFrigate has 16 prisms
    bridge-crew:
    - __admin: Commander
    - vice: Lieutenant
    - tactical: Sergeant
    - science: Ensign
    - medical: Ensign
    - engineer: Ensign
    standard-crew:
    - 3 Lance 
    - 3 Corporal
    - 4 Private

    """
    @staticmethod
    def build_frigate_ship(ship_type: int):
        ship_index = abs(ship_type) % 3

        lead_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 2])
        vice_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 3])
        tactical_officer = PrismDrone(rank=LEGION_RANKS[5])
        science_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])
        medical_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])
        engineer_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])

        crew = list()
        for i in range(3):
            crew.append(PrismDrone(rank=LegionRank.Lance))
            crew.append(PrismDrone(rank=LegionRank.Corporal))
            crew.append(PrismDrone(rank=LegionRank.Private))
        crew.append(PrismDrone(rank=LegionRank.Private))

        ship = StarFrigate(
            lead_officer=lead_officer,
            vice_officer=vice_officer,
            tactical_officer=tactical_officer,
            science_officer=science_officer,
            medical_officer=medical_officer,
            engineer_officer=engineer_officer,
            crew=crew
        )
        return ship

    """
    total is 12 prisms

    ex.) StarCruiser has 12 prisms
    bridge-crew:
    - __admin: Lieutenant
    - vice: Sergeant
    - tactical: Sergeant
    - science: Ensign
    - medical: Ensign
    - engineer: Ensign
    standard-crew:
    - 1 Lance 
    - 2 Corporal
    - 3 Private

    """
    @staticmethod
    def build_cruiser_ship(ship_type: int):
        ship_index = abs(ship_type) % 4

        lead_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 2])
        vice_officer = PrismDrone(rank=LEGION_RANKS[ship_index + 3 if ship_index + 3 <= 5 else 5])
        tactical_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index <= 1 else 5])
        science_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])
        medical_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])
        engineer_officer = PrismDrone(rank=LEGION_RANKS[4 if ship_index == 0 else 6])

        crew = list()
        for i in range(3):
            if i == 0:
                crew.append(PrismDrone(rank=LegionRank.Lance))
            if i <= 1:
                crew.append(PrismDrone(rank=LegionRank.Corporal))
            crew.append(PrismDrone(rank=LegionRank.Private))

        ship = StarCruiser(
            lead_officer=lead_officer,
            vice_officer=vice_officer,
            tactical_officer=tactical_officer,
            science_officer=science_officer,
            medical_officer=medical_officer,
            engineer_officer=engineer_officer,
            crew=crew
        )

        return ship

    def __init__(self, fleet_leader: PrismDrone = None, leader_flagship: StarShip = None):
        if leader_flagship is None:
            leader_flagship = LegionFleet.build_capital_ship(0)
        if fleet_leader is None:
            fleet_leader = leader_flagship.lead_officer

        self.fleet_leader = fleet_leader
        self.fleet_flagship = leader_flagship

        ships = (
            self.fleet_flagship,
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

        self.__ships = { ship.id: ship for ship in ships }

    def ships(self):
        return self.__ships

    def cruiser_ships(self):
        cruiser_ships = find_fleet_ships_by_type(self, StarCruiser)
        return cruiser_ships

    def frigate_ships(self):
        frigate_ships = find_fleet_ships_by_type(self, StarFrigate)
        return frigate_ships

    def capital_ships(self):
        capital_ships = find_fleet_ships_by_type(self, StarCapital)
        return capital_ships

class AdminFleet(LegionFleet):
    """
    total is 25 prisms

    ex.) StarDreadnought has 26 prisms
    bridge-crew: Vice Admin decides who becomes an Arch in LegionArmada while Admin decides who becomes Vice, General, and Admiral
    - __admin: Arch as Vice Admin as best Skilled Arch in Guardianship
    - vice: Major as best Skilled worker in Legion before becoming Guardian
    - tactical: Major as best Tactical Skilled worker in Legion
    - science: Major as best Tactical Skilled worker in Legion
    - medical: Major as best Tactical Skilled worker in Legion
    - engineer: Major as best Tactical Skilled worker in Legion
    standard-crew:
    - 4 Captains as best Captains of Admin Legion
    - 4 Commanders as best Commanders of Admin Legion
    - 4 Lieutenants as best Lieutenants of Admin Legion
    - 4 Sergeants as best Sergeants of Admin Legion
    - 4 Ensigns as best Ensigns of Admin Legion

    """
    @staticmethod
    def build_dreadnought_ship(lead_officer: PrismDrone = None):
        if lead_officer is None:
            lead_officer = PrismDrone(rank=LegionRank.Arch)

        crew = list()
        for _ in range(4):
            crew.append(PrismDrone(rank=LegionRank.Captain))
            crew.append(PrismDrone(rank=LegionRank.Commander))
            crew.append(PrismDrone(rank=LegionRank.Lieutenant))
            crew.append(PrismDrone(rank=LegionRank.Sergeant))
            crew.append(PrismDrone(rank=LegionRank.Ensign))

        ship = StarDreadnought(
            lead_officer=lead_officer,
            vice_officer=PrismDrone(rank=LegionRank.Major),
            tactical_officer=PrismDrone(rank=LegionRank.Major),
            science_officer=PrismDrone(rank=LegionRank.Major),
            medical_officer=PrismDrone(rank=LegionRank.Major),
            engineer_officer=PrismDrone(rank=LegionRank.Major),
            crew=crew
        )

        return ship

    def __init__(self, admin_leader: PrismDrone, vice_leader: PrismDrone):
        super().__init__(
            fleet_leader=admin_leader,
            leader_flagship=AdminFleet.build_dreadnought_ship(vice_leader))

    def dreadnought_ship(self):
        return self.fleet_flagship
