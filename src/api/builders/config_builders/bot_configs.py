from src.api.builders.config_builders.drone_configs import build_drone_config
from src.api.helpers.alias_helper import create_alias
from src.utils.configs.bot_configs import BotConfig
from src.utils.configs.bot_configs.server_config import ServerConfig


def build_bot_config(version: int, name: str, alias: str = None) -> BotConfig:
    if alias is None:
        alias = create_alias(name=name)
    drone_config = build_drone_config(
        version=version,
        name=name,
        alias=alias,
    )
    return BotConfig(drone=drone_config)


def build_server_config(version: int, name: str, alias: str = None) -> ServerConfig:
    if alias is None:
        alias = create_alias(name=name)
    drone_config = build_drone_config(
        version=version,
        name=name,
        alias=alias
    )
    return ServerConfig(drone=drone_config)

