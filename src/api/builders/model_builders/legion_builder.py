from src.api.builders.config_builders.legion_configs import build_legion_config
from src.models.legion import Legion
from src.utils.configs.model_configs.drone_config import DroneConfig


def build_legion(
    version: int,
    name: str,
    leader_config: DroneConfig,
    vice_config: DroneConfig,
    general_config: DroneConfig,
    admiral_config: DroneConfig
) -> Legion:
    legion_config = build_legion_config(
        version=version,
        name=name,
        leader_config=leader_config,
        vice_config=vice_config,
        general_config=general_config,
        admiral_config=admiral_config
    )

    return Legion(config=legion_config)

