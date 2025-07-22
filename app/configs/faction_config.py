from uuid import UUID

from app.configs import Config
from utils.enums.faction_enums import FactionType


class FactionConfig(Config):
    faction_type: FactionType
    leader_id: UUID
    fortress_id: UUID
    stats: FactionStats

