from typing import List

from src.api.builders.config_builders.user_configs.brian_config import build_brian_config
from src.api.builders.config_builders.user_configs.emma_config import build_emma_config
from src.api.builders.config_builders.user_configs.mary_config import build_mary_config
from src.api.builders.config_builders.user_configs.max_config import build_max_config
from src.api.builders.config_builders.user_configs.payton_config import build_payton_config
from src.api.builders.config_builders.user_configs.tyler_config import build_tyler_config
from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.api.builders.model_builders.user_builder import build_users
from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants import DEV_VERSION, PROD_VERSION, DEBUG_VERSION
from src.utils.user import User


def get_user_configs(version: int) -> List[UserConfig]:
    user_configs = []
    if version >= DEV_VERSION:
        user_configs.append(build_wes_config(version=version))
        user_configs.append(build_emma_config(version=version))
        user_configs.append(build_mary_config(version=version))
        user_configs.append(build_max_config(version=version))
    if version > PROD_VERSION:
        user_configs.append(build_tyler_config(version=version))
        user_configs.append(build_payton_config(version=version))
        user_configs.append(build_brian_config(version=version))
    return user_configs


def get_users(version: int) -> List[User]:
    user_configs = get_user_configs(version=version)
    user_list = build_users(configs=user_configs)
    return user_list

