from src.models.user import User
from src.utils.configs.user_config import UserConfig


def build_user(config: UserConfig) -> User:
    return User(config=config)

