from typing import List

from src.api.builders.app_builders import build_prism_hive, build_prism_reflect
from src.api.builders.config_builders.bot_configs import build_server_config
from src.api.builders.model_builders.bot_builder import build_hedron_server
from src.prism_net import PrismNet
from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.app_builders.tool_builders import build_prism_lab, build_prism_forge, build_prism_studio
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.configs.net_config import NetConfig
from src.utils.user import User

def build_net_config(net_version: int, user_configs: List[UserConfig]) -> NetConfig:
    return NetConfig(
        version=net_version,
        user_configs=user_configs,
    )

def build_prism_net(net_version: int, users: List[User]) -> PrismNet:
    user_configs = []
    for user in users:
        user_configs.append(user.config)
    net_config = build_net_config(net_version=net_version, user_configs=user_configs)
    prism_net = PrismNet(
        config=net_config,
        hedron=build_hedron_server(config=build_server_config())
    )
    return prism_net


def build_mvp(mvp_version: int, users: List[User] = None) -> PrismNet:
    if users is None:
        users = []

    mvp = build_prism_net(net_version=mvp_version, users=users)
    return mvp

