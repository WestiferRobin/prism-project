from typing import List

from src.utils.user import User
from src.utils.configs.model_configs.user_config import UserConfig


def build_user(config: UserConfig) -> User:
    return User(config=config)


def build_user_list(configs: List[UserConfig]) -> List[User]:
    users = []
    for config in configs:
        user = build_user(config=config)
        users.append(user)

    return users

