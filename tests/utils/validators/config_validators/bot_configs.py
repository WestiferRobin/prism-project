from uuid import UUID

from utils.validators.config_validators import validate_config
from utils.validators.config_validators.drone_configs import validate_drone_config
from src.utils.configs.bot_configs import BotConfig
from src.utils.configs.model_configs.drone_config import DroneConfig


def validate_bot_config(config: BotConfig, expected_value: BotConfig) -> None:
    assert config is not None
    assert expected_value is not None
    assert isinstance(config, BotConfig)
    validate_config(source_config=config, target_config=expected_value)

    assert config.drone is not None
    assert isinstance(config.drone, DroneConfig)
    validate_drone_config(source_config=config.drone)

    assert config.id is not None
    assert isinstance(config.id, UUID)

    assert config.name is not None
    assert isinstance(config.name, str)
