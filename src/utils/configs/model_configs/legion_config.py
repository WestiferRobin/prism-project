from src.utils.configs import Config
from src.utils.configs.model_configs.drone_config import DroneConfig


class LegionConfig(Config):
    admin_config: DroneConfig
    vice_config: DroneConfig
    general_config: DroneConfig
    admiral_config: DroneConfig

    def __init__(self, **legion_data):
        super().__init__(**legion_data)

