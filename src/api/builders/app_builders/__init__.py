from src.api.builders.config_builders.app_configs import build_app_config
from src.app import App
from src.utils.configs.app_configs import AppConfig
from src.utils.enums.platform_enums import PlatformType


def build_app(config: AppConfig) -> App:
    return App(config=config)


def build_prism_reflect(version: int, platform: PlatformType = PlatformType.Mobile) -> App:
    config = build_app_config(version=version, name="Prism Reflect", alias="prism-reflect", platform=platform)
    return build_app(config=config)


def build_prism_hive(version: int, platform: PlatformType = PlatformType.Web) -> App:
    config = build_app_config(version=version, name="Prism Hive", alias="prism-hive", platform=platform)
    return build_app(config=config)

