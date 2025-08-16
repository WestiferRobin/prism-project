from typing import List

from src.api.builders.config_builders.legion_configs import build_faction_config
from src.api.builders.model_builders.legion_builder import build_legion
from src.models.colonies.legion_colony import LegionColony
from src.models.legion.faction import Faction
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.faction_config import FactionConfig
from src.utils.enums.game_enums.faction_enums import FactionType


def build_faction_colonies(config: FactionConfig) -> List[LegionColony]:
    configs = [
        config.admin_config,
        config.vice_config,
        config.general_config,
        config.admiral_config
    ]

    colonies = []
    for leader_config in configs:
        pass

    return colonies


def build_faction_armada(config: FactionConfig) -> LegionArmada:


def build_faction(
    version: int,
    faction_type: FactionType,
    leader_config: DroneConfig,
    vice_config: DroneConfig,
    general_config: DroneConfig,
    admiral_config: DroneConfig
) -> Faction:
    faction_config = build_faction_config(
        version=version,
        faction_type=faction_type,
        leader_config=leader_config,
        vice_config=vice_config,
        general_config=general_config,
        admiral_config=admiral_config
    )

    faction_colonies = build_faction_colonies(
        version=version,
        faction_config=faction_config,
    )

    return Faction(
        config=faction_config
    )

