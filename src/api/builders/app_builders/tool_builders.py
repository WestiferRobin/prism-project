from src.api.builders.app_builders import build_prism_app
from src.api.builders.config_builders.app_configs import build_app_config
from src.app import App
from src.utils.enums.platform_enums import PlatformType


def build_prism_forge(platform: PlatformType = PlatformType.Web, version: int = 0) -> App:
    config = build_app_config(version=version, alias="prism-forge", name="Prism Forge", platform=platform)
    return build_prism_app(config=config)


def build_prism_lab(platform: PlatformType = PlatformType.Web, version: int = 0) -> App:
    config = build_app_config(version=version, alias="prism-lab", name="Prism Lab", platform=platform)
    return build_prism_app(config=config)


def build_prism_reflect(platform: PlatformType = PlatformType.Mobile, version: int = 0) -> App:
    config = build_app_config(version=version, alias="prism-reflect", name="Prism Reflect", platform=platform)
    return build_prism_app(config=config)


def build_prism_studio(platform: PlatformType = PlatformType.Web, version: int = 0) -> App:
    config = build_app_config(version=version, alias="prism-studio", name="Prism Studio", platform=platform)
    return build_prism_app(config=config)

