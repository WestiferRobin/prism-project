from utils.configs import Config
from utils.configs.vehicle_config import VehicleConfig


def validate_config(config: Config):
    assert config is not None
    assert isinstance(config, Config)

    assert config.name is not None
    assert isinstance(config.name, str)


def validate_vehicle_config(config: VehicleConfig):
    validate_config(config)

