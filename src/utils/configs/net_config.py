from typing import List

from src.utils.configs import Config
from src.utils.configs.model_configs.user_config import UserConfig


class NetConfig(Config):
    user_configs: List[UserConfig]

    def __init__(self, **net_data):
        super().__init__(name="Prism.net", alias="prism_config-net", **net_data)

