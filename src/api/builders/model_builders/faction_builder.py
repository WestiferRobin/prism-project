from src.models.legion.faction import Faction
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.enums.game_enums.faction_enums import FactionType

def build_faction(
    version: int,
    faction_type: FactionType,
    leader_config: DroneConfig,
    vice_config: DroneConfig,
    general_config: DroneConfig,
    admiral_config: DroneConfig
) -> Faction:
    legion = build_legion()

