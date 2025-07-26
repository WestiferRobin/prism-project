from uuid import UUID, uuid4

from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants import AVATAR_ID


def build_user_config(name: str, user_id: UUID = uuid4()) -> UserConfig:
    return UserConfig(
        name=name,
        user_id=user_id,
    )


def build_wes_config() -> UserConfig:
    wes_id = AVATAR_ID
    return build_user_config("Wes", wes_id)


def build_emma_config() -> UserConfig:
    return build_user_config("Emma")


def build_mary_config() -> UserConfig:
    return build_user_config("Mary")


def build_max_config() -> UserConfig:
    return build_user_config("Max")

