from uuid import UUID

from utils.configs import Config
from utils.enums.faction_enums import FactionType


class FactionConfig(Config):
    faction_type: FactionType
    leader_id: UUID
    fortress_id: UUID
    stats: FactionStats

