from typing import Tuple

from src.models.drones.model import PrismDrone
from src.models.vehicles.model import LightEngine
from src.models.vehicles.ships.space_ships import OrbDrone, SpaceFighter, SpaceShuttle, SpaceSpeeder
from src.utils.enums.prism_enums import DroneRank


class StarShip:
    def __init__(
            self,
            lead_officer: PrismDrone,
            first_officer: PrismDrone,
            second_officer: PrismDrone,
    ):
        self.id = lead_officer.id
        self.engines = (
            LightEngine(self.id),
            LightEngine(self.id),
            LightEngine(self.id),
            LightEngine(self.id)
        )

        self.lead_officer = lead_officer
        self.first_officer = first_officer
        self.second_officer = second_officer

        self.crew = (
            lead_officer,
            first_officer,
            second_officer,
            PrismDrone(rank=DroneRank.Private),
            PrismDrone(rank=DroneRank.Private),
            PrismDrone(rank=DroneRank.Corporal),
            PrismDrone(rank=DroneRank.Private),
            PrismDrone(rank=DroneRank.Lance),
            PrismDrone(rank=DroneRank.Ensign)
        )

        self.grid = {
            "hanger": (
                SpaceFighter(self.crew[3]),
                SpaceFighter(self.crew[4]),
                SpaceShuttle(self.crew[5], self.crew[6])
            ),
            "cargo": (OrbDrone(self.crew[8].brain), SpaceSpeeder(self.crew[7])),
            "bridge": (self.crew[0], self.crew[1], self.crew[2], self.crew[8])
        }


class StarCruiser(StarShip): # Outposts, Camps
    def __init__(self, lead_officer=None, first_officer=None, second_officer=None):
        if lead_officer is None:
            lead_officer = PrismDrone(rank=DroneRank.Lieutenant)
        elif first_officer is None:
            first_officer = PrismDrone(rank=DroneRank.Sergeant)
        elif second_officer is None:
            second_officer = PrismDrone(rank=DroneRank.Sergeant)
        super().__init__(lead_officer, first_officer, second_officer)


class StarFrigate(StarShip): # Town, Outposts
    def __init__(self, lead_officer=None, first_officer=None, second_officer=None):
        if lead_officer is None:
            lead_officer = PrismDrone(rank=DroneRank.Commander)
        elif first_officer is None:
            first_officer = PrismDrone(rank=DroneRank.Lieutenant)
        elif second_officer is None:
            second_officer = PrismDrone(rank=DroneRank.Sergeant)
        super().__init__(lead_officer, first_officer, second_officer)


class StarCapital(StarShip): # City, Town
    def __init__(self, lead_officer=None, first_officer=None, second_officer=None):
        if lead_officer is None:
            lead_officer = PrismDrone(rank=DroneRank.Captain)
        elif first_officer is None:
            first_officer = PrismDrone(rank=DroneRank.Commander)
        elif second_officer is None:
            second_officer = PrismDrone(rank=DroneRank.Lieutenant)
        super().__init__(lead_officer, first_officer, second_officer)


class StarDreadnought(StarShip): # Citadel
    def __init__(self, lead_officer=None, first_officer=None, second_officer=None):
        if lead_officer is None:
            lead_officer = PrismDrone(rank=DroneRank.Arch)
        elif first_officer is None:
            first_officer = PrismDrone(rank=DroneRank.Major)
        elif second_officer is None:
            second_officer = PrismDrone(rank=DroneRank.Commander)
        super().__init__(lead_officer, first_officer, second_officer)

