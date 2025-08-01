from typing import List

from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.exceptions import PrismException


def build_user_config(
    avatar_config: DroneConfig,
    companion_config: DroneConfig,
    account_configs: List[AccountConfig] = None,
) -> UserConfig:
    if avatar_config.version != companion_config.version:
        raise PrismException(f"avatar and companion configs don't match for a valid user config")

    if account_configs is None:
        account_configs = []

    return UserConfig(
        version=avatar_config.version,
        config_id=avatar_config.id,
        name=avatar_config.name,
        alias=avatar_config.alias,
        avatar_config=avatar_config,
        companion_config=companion_config,
        account_configs=account_configs,
    )
