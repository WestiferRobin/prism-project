from typing import List

from src.api.builders.model_builders.user_builder import build_users
from src.api.builders.net_builder import build_prism_net
from src.prism_net import PrismNet
from src.utils.configs.model_configs.user_config import UserConfig


def build_mvp(
    version: int,
    user_configs: List[UserConfig]
) -> PrismNet:
    users = build_users(configs=user_configs)
    user_apps = get_user_apps(user_configs=user_configs)
    user_bots = get_user_bots(user_configs=user_configs)
    mvp = build_prism_net(
        version=version,
        users=users,
        apps=user_apps,
        bots=user_bots
    )
    return mvp

