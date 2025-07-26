from src.utils.configs import Config
from src.utils.configs.model_configs.drone_config import DroneConfig


class LegionConfig(Config):
    admin: DroneConfig
    vice: DroneConfig
    general: DroneConfig
    admiral: DroneConfig

