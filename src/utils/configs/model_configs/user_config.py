from typing import List

from src.utils.configs import Config
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.configs.model_configs.drone_config import DroneConfig


class UserConfig(Config):
    avatar_config: DroneConfig
    companion_config: DroneConfig
    account_configs: List[AccountConfig] = []

    def __init__(self, **drone_data):
        super().__init__(**drone_data)

