from src.api.helpers.alias_helper import configure_alias
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.faction_config import FactionConfig
from src.utils.configs.model_configs.legion_config import LegionConfig
from src.utils.enums.game_enums.faction_enums import FactionType


def build_legion_config(
    version: int,
    name: str,
    leader_config: DroneConfig,
    vice_config: DroneConfig,
    general_config: DroneConfig,
    admiral_config: DroneConfig
) -> LegionConfig:
    return LegionConfig(
        version=version,
        name=name,
        alias=configure_alias(name),
        leader_config=leader_config,
        vice_config=vice_config,
        general_config=general_config,
        admiral_config=admiral_config
    )

