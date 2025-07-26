from src.prism_net import PrismNet
from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.app_builders.iot_builder import build_hedron_bot, build_avatar_legion, build_hedron_hive
from src.api.builders.app_builders.tool_builders import build_prism_lab, build_prism_reflect, build_prism_forge
from src.utils.configs.model_configs.user_config import UserConfig


def build_prism_net(version: int, owner_config: UserConfig) -> PrismNet:
    apps = [
        build_solar_conquest(version=version),
        build_prism_lab(version=version),
        build_prism_forge(version=version),
        build_prism_reflect(version=version)
    ]
    prism_net = PrismNet(
        version=version,
        apps=apps,
        server=build_hedron_hive(version=version),
        bot=build_hedron_bot(version=version),
        avatar_legion=build_avatar_legion(avatar_config=owner_config)
    )
    return prism_net


def build_mvp(config: UserConfig) -> PrismNet:
    mvp = build_prism_net(version=config.version, owner_config=config)
    return mvp

