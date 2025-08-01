from typing import List

from src.api.builders.net_builder import build_prism_net
from src.app import App
from src.models.bots import Bot
from src.prism_net import PrismNet
from src.utils.user import User


def build_mvp(
    version: int,
    users: List[User],
    apps: List[App],
    bots: List[Bot]
) -> PrismNet:
    mvp = build_prism_net(
        version=version,
        users=users,
        apps=apps,
        bots=bots
    )
    return mvp

