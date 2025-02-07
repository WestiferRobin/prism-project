import uuid
from typing import Tuple

from src.models.drones.model import PrismDrone, PrismAvatar
from src.models.vehicles.ships.star_ships import StarShip, DreadnoughtShip, CapitalShip, FrigateShip, CruiserShip


class LegionFleet:
    def __init__(self, leader: PrismDrone, ships: Tuple[StarShip] = None):
        if ships is None:
            ships = (
                DreadnoughtShip(),
                CapitalShip(),
                FrigateShip(),
                CruiserShip()
            )
        self.leader = leader
        self.ships = ships


class LegionArmada:
    def __init__(self, leader: PrismDrone):
        self.fleets = [LegionFleet(leader)]


class AdminLegion:
    def __init__(self, username: str, user_id=None):
        if user_id is None:
            user_id = uuid.uuid4()
        self.username = username
        self.leader = PrismAvatar(avatar_sprite=username[0], user_id=user_id)
        self.armada = LegionArmada(self.leader)
        # TODO: Figure out how to add bases with Sol and Armada
        # TODO: Figure out campaign with Sov in Prequel Wars
        # TODO: Figure out Galaxy campaign in Walker Saga

    def __str__(self):
        return f"{self.username}'s LegionArmada"
