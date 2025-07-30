from src.api.builders.app_builders import build_prism_hive, build_prism_reflect
from src.prism_net import PrismNet
from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.app_builders.tool_builders import build_prism_lab, build_prism_forge, build_prism_studio
from src.utils.configs.model_configs.user_config import UserConfig


def build_prism_net(version: int, owner_config: UserConfig) -> PrismNet:
    apps = [
        build_solar_conquest(version=version),
        build_prism_lab(version=version),
        build_prism_forge(version=version),
        build_prism_studio(version=version),
        build_prism_reflect(version=version),
        build_prism_hive(version=version),
    ]
    prism_net = PrismNet(
        version=version,
        apps=apps,
        server=build_hedron_hive(version=version),
        bot=build_hedron_bot(version=version),
        avatar_legion=build_avatar_legion(version=version, avatar_config=owner_config)
    )
    return prism_net


def build_mvp(config: UserConfig) -> PrismNet:
    mvp = build_prism_net(version=config.version, owner_config=config)
    return mvp

