from typing import List

from src.api.services.app_service import get_user_accounts
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.exceptions import PrismException


def build_user_config(
    avatar_config: DroneConfig,
    companion_config: DroneConfig,
) -> UserConfig:
    if avatar_config.version != companion_config.version:
        raise PrismException(f"avatar and companion configs don't match for a valid user config")

    account_configs = get_user_accounts(user_id=avatar_config.id, version=avatar_config.version)
    return UserConfig(
        avatar_config=avatar_config,
        companion_config=companion_config,
        account_configs=account_configs,
    )
