from src.api.builders.model_builders.drone_builder import build_legion_drone, build_drone
from src.api.builders.model_builders.prism_builders import build_prism
from src.models.drones import Drone
from src.models.drones.legion_drone import LegionDrone
from src.models.prisms import Prism
from src.utils.configs.model_configs.user_config import UserConfig


def build_avatar_prism(config: UserConfig) -> Prism:
    return build_prism(config=config)


def build_avatar_drone(config: UserConfig) -> Drone:
    return build_drone(
        version=config.version,
        name=config.name,
        alias=config.alias
    )


def build_avatar_legion_drone(config: UserConfig) -> LegionDrone:
    return build_legion_drone(
        version=config.version,
        name=config.name,
        alias=config.alias
    )

