from typing import List

from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.configs.model_configs.drone_config import DroneConfig


class UserConfig(DroneConfig):
    avatar_config: DroneConfig
    companion_config: DroneConfig
    account_configs: List[AccountConfig] = []

    def __init__(self,
        avatar_config: DroneConfig,
        **drone_data
    ):
        super().__init__(
            prism_config=avatar_config.prism_config,
            avatar_config=avatar_config,
            **drone_data
        )

