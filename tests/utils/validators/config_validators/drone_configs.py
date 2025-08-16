from uuid import UUID

from utils.validators.config_validators.prism_configs import validate_prism_config
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.prism_config import PrismConfig


def validate_drone_config(source_config: DroneConfig, target_config: DroneConfig):
    assert source_config is not None
    assert type(source_config) is DroneConfig

    assert source_config.version == target_config.version
    assert type(source_config.id) is UUID
    assert type(source_config.name) is str
    assert type(source_config.alias) is str

    assert source_config.prism_config is not None
    assert type(source_config.prism_config) is PrismConfig
    validate_prism_config(
        source_config=source_config.prism_config,
        target_config=target_config.prism_config
    )

