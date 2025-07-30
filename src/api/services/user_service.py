from typing import List

from src.api import build_wes_config, build_user
from src.utils.constants import INITIAL_VERSION
from src.utils.user import User


def get_initial_users(version: int = INITIAL_VERSION) -> List[User]:
    user_configs = [ build_wes_config(version=version) ]

    users = []
    for user_config in user_configs:
        user = build_user(config=user_config)
        users.append(user)

    return users


def get_alpha_users(version: int = ) -> List[User]:

