from pydantic import BaseModel

from src.models.drones.prism_drone import PrismDrone
from src.utils.enums.game_enums.faction_enums import FactionType


class Faction(BaseModel):
    flag: FactionType
    leader: PrismDrone

