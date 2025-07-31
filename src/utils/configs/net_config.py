from typing import List

from src.utils.configs import Config
from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.user_config import UserConfig


class NetConfig(Config):
    app_configs: List[AppConfig]
    user_configs: List[UserConfig]

    def __init__(self, **net_data):
        super().__init__(name="Prism.net", alias="prism_config-net", **net_data)

