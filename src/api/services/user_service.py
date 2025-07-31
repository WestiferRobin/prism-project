from typing import List

from src.api import build_wes_config, build_user, build_emma_config, build_mary_config, build_max_config
from src.api.builders.config_builders.user_configs import build_tyler_config, build_payton_config, build_brian_config
from src.api.builders.model_builders.user_builder import build_user_list
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants import LAMBDA_VERSION, ALPHA_VERSION, BETA_VERSION, GAMMA_VERSION, OMEGA_VERSION
from src.utils.user import User


def get_user_configs(version: int) -> List[UserConfig]:
    users = []
    if version >= LAMBDA_VERSION:
        users.append(build_wes_config(version=version))
        users.append(build_mary_config(version=version))
    if version >= ALPHA_VERSION:
        users.append(build_emma_config(version=version))
        users.append(build_max_config(version=version))
    if version >= BETA_VERSION:
        users.append(build_tyler_config(version=version))
    if version >= GAMMA_VERSION:
        users.append(build_payton_config(version=version))
    if version >= OMEGA_VERSION:
        users.append(build_brian_config(version=version))
    return users


def get_initial_users(version: int = LAMBDA_VERSION) -> List[User]:
    user_configs = get_user_configs(version=version)
    return build_user_list(configs=user_configs)


def get_alpha_users(version: int = ALPHA_VERSION) -> List[User]:
    user_configs = get_user_configs(version=version)
    return build_user_list(configs=user_configs)


def get_beta_users(version: int = BETA_VERSION) -> List[User]:
    user_configs = get_user_configs(version=version)
    return build_user_list(configs=user_configs)


def get_demo_users(version: int = GAMMA_VERSION) -> List[User]:
    user_configs = get_user_configs(version=version)
    return build_user_list(configs=user_configs)


def get_final_users(version: int = OMEGA_VERSION) -> List[User]:
    user_configs = get_user_configs(version=version)
    return build_user_list(configs=user_configs)

