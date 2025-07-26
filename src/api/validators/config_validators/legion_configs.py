from src.api.validators.config_validators import validate_config
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.legion_config import LegionConfig


def validate_legion_config(config: LegionConfig):
    assert config is not None
    assert isinstance(config, LegionConfig)
    validate_config(config=config)

    assert config.admin is not None
    assert isinstance(config.admin, DroneConfig)

    assert config.vice is not None
    assert isinstance(config.vice, DroneConfig)

    assert config.general is not None
    assert isinstance(config.general, DroneConfig)

    assert config.admiral is not None
    assert isinstance(config.admiral, DroneConfig)

