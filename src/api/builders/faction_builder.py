from src.models.drones.prism_drone import PrismDrone
from src.models.factions import Faction
from src.utils.enums.game_enums.faction_enums import FactionType


def build_faction(faction_type: FactionType, leader: PrismDrone = None) -> Faction:

    return Faction(flag=faction_type, leader=PrismDrone())

