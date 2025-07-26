from src.api.builders.config_builders.prism_configs import build_prism_config
from src.api.helpers.alias_helper import create_alias
from src.utils.configs.model_configs.drone_config import DroneConfig


def build_drone_config(version: int, name: str, alias: str = None) -> DroneConfig:
    if alias is None:
        alias = create_alias(name=name)
    prism_config = build_prism_config(
        version=version,
        name=name,
        alias=alias
    )
    return DroneConfig(prism=prism_config)

