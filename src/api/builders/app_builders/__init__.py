from src.api.builders.config_builders.app_configs import build_app_config
from src.app import App
from src.utils.configs.app_configs import AppConfig
from src.utils.enums.platform_enums import PlatformType


def build_prism_app(config: AppConfig) -> App:
    return App(config=config)


def build_prism_hive(platform: PlatformType = PlatformType.Web) -> App:
    config = build_app_config("Prism Hive", platform=platform)
    return build_prism_app(config=config)

