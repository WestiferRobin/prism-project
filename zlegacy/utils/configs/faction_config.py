from uuid import UUID

from src.utils.configs import Config
from src.utils.enums.faction_enums import FactionType


class FactionConfig(Config):
    faction_type: FactionType
    leader_id: UUID
    fortress_id: UUID
    stats: FactionStats

