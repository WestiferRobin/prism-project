from typing import List

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.configs.net_config import NetConfig


def build_net_config(
    version: int,
    user_configs: List[UserConfig],
    app_configs: List[AppConfig],
) -> NetConfig:
    return NetConfig(
        version=version,
        app_configs=app_configs,
        user_configs=user_configs,
    )

