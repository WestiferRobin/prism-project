from uuid import UUID

from src.api.validators.config_validators import validate_config
from src.api.validators.config_validators.drone_configs import validate_drone_config
from src.utils.configs.bot_configs import BotConfig
from src.utils.configs.model_configs.drone_config import DroneConfig


def validate_bot_config(config: BotConfig):
    assert config is not None
    assert isinstance(config, BotConfig)
    validate_config(config=config)

    assert config.drone is not None
    assert isinstance(config.drone, DroneConfig)
    validate_drone_config(config=config.drone)

    assert config.id is not None
    assert isinstance(config.id, UUID)

    assert config.name is not None
    assert isinstance(config.name, str)
