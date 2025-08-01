from typing import List

from src.api.builders.config_builders.net_configs import build_net_config
from src.app import App
from src.models.bots import Bot
from src.prism_net import PrismNet
from src.utils.user import User


def build_prism_net(
    version: int,
    users: List[User],
    apps: List[App],
    bots: List[Bot]
) -> PrismNet:
    net_config = build_net_config(
        version=version,
        user_configs=[user.config for user in users],
        app_configs=[app.config for app in apps],
        bot_configs=[bot.config for bot in bots]
    )

    prism_net = PrismNet(
        config=net_config,
        users=users,
        apps=apps,
        bots=bots
    )
    return prism_net