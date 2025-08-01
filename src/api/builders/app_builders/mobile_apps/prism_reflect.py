from src.api.builders.app_builders import build_app
from src.api.builders.config_builders.app_configs import build_app_config
from src.app import App
from src.utils.enums.platform_enums import PlatformType


def build_prism_reflect(version: int, platform: PlatformType = PlatformType.Mobile) -> App:
    config = build_app_config(
        version=version,
        app_name="Prism Reflect",
        app_alias="prism-reflect",
        platform=platform
    )
    return build_app(config=config)

