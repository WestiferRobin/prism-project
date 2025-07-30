from typing import List

from src.api.builders.app_builders import build_prism_hive, build_prism_reflect
from src.prism_net import PrismNet
from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.app_builders.tool_builders import build_prism_lab, build_prism_forge, build_prism_studio
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.user import User


def build_prism_net(net_version: int, users: List[User]) -> PrismNet:
    prism_net = PrismNet(
        version=net_version,
        users=users
    )
    return prism_net


def build_mvp(mvp_version: int, users: List[UserConfig] = None) -> PrismNet:
    if users is None:
        users = []

    mvp = build_prism_net(version=mvp_version, users=users)
    return mvp

