from src.api.validators.config_validators import validate_config
from src.api.validators.config_validators.prism_configs import validate_prism_config
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.prism_config import PrismConfig


def validate_drone_config(config: DroneConfig):
    assert config is not None
    assert isinstance(config, DroneConfig)
    validate_config(config=config)

    assert config.prism_config is not None
    assert isinstance(config.prism_config, PrismConfig)
    validate_prism_config(config=config.prism_config)

