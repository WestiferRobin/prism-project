from typing import List

from src.api.builders.config_builders.user_configs import build_wes_config, build_emma_config, build_mary_config, \
    build_max_config
from src.api.builders.user_builder import build_user
from src.models.user import User


def get_mvp_users() -> List[User]:
    return [
        build_user(config=build_wes_config()),
        build_user(config=build_emma_config()),
        build_user(config=build_mary_config()),
        build_user(config=build_max_config())
    ]

