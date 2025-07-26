from src import PrismNet
from src.api.builders.app_builders.iot_builder import build_hedron_bot, build_avatar_legion, build_hedron_hive
from src.api.builders.app_builders.tool_builders import build_prism_lab, build_prism_reflect, build_prism_forge
from src.utils.configs.user_config import UserConfig
from zlegacy.api.builders import build_solar_conquest


def build_prism_net(version: int, owner_config: UserConfig) -> PrismNet:
    apps = []
    bots = []

    if version <= 0:
        apps.append(build_solar_conquest(version=version))
        apps.append(build_prism_lab(version=version))
    if version == 1:
        apps.append(build_prism_reflect(version=version))
        bots.append(build_hedron_hive(version=version))
    if version == 2:
        apps.append(build_prism_forge(version=version))
        bots.append(build_hedron_bot(version=version))
    if version >= 3:
        bots.append(build_avatar_legion(avatar_config=owner_config))

    return PrismNet(version=version, apps=apps, bots=bots)


def build_mvp(config: UserConfig) -> PrismNet:
    mvp = build_prism_net(version=config.version, owner_config=config)
    return mvp

