from typing import List

from src.api.builders.app_builders import build_prism_hive, build_prism_reflect
from src.api.builders.config_builders import build_net_config
from src.api.builders.config_builders.bot_configs import build_server_config
from src.api.builders.model_builders.bot_builder import build_hedron_server, build_bot_speeder
from src.prism_net import PrismNet
from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.app_builders.tool_builders import build_prism_lab, build_prism_forge, build_prism_studio
from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.user_config import UserConfig


def build_prism_net(
    version: int,
    user_configs: List[UserConfig],
    app_configs: List[AppConfig]
) -> PrismNet:
    net_config = build_net_config(
        version=version,
        user_configs=user_configs,
        app_configs=app_configs
    )

    hedron_server = build_hedron_server(
        version=version,
        owner_config=user_configs[0],
        companion_config=user_configs[0].companion_config,
    )
    bot_speeder = build_bot_speeder(
        version=version,
    )
    bot_legion = build_bot_legion(
        version=version,
    )

    prism_net = PrismNet(
        config=net_config,
        hedron=hedron_server,
        speeder=bot_speeder,
        legion=bot_legion
    )
    return prism_net


def build_mvp(version: int, user_configs: List[UserConfig]) -> PrismNet:
    mvp = build_prism_net(version=version, user_configs=user_configs)
    return mvp

