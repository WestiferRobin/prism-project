from typing import List, Dict
from uuid import UUID

from src.api.builders.config_builders.app_configs import build_app_config
from src.app import App
from src.utils.configs.app_configs import AppConfig
from src.utils.enums.platform_enums import PlatformType


def build_app(config: AppConfig) -> App:
    return App(config=config)


def build_app_list(configs: List[AppConfig]) -> List[App]:
    apps = []
    for config in configs:
        app = build_app(config=config)
        apps.append(app)
    return apps


def build_app_registry(configs: List[AppConfig]) -> Dict[UUID, App]:
    registry = {}
    apps = build_app_list(configs=configs)
    for app in apps:
        registry[app.id] = app
    return registry


def build_prism_cook(version: int, app_id: UUID = None, platform: PlatformType = PlatformType.Mobile) -> App:
    config = build_app_config(
        version=version,
        app_name="Prism Forge",
        app_alias="prism-cook",
        platform=platform,
        app_id=app_id
    )
    return build_app(config=config)


def build_prism_hive(version: int, app_id: UUID = None, platform: PlatformType = PlatformType.Web) -> App:
    config = build_app_config(
        version=version,
        app_name="Prism Hive",
        app_alias="prism-hive",
        platform=platform,
        app_id=app_id
    )
    return build_app(config=config)


def build_big_button(version: int, app_id: UUID = None, platform: PlatformType = PlatformType.Mobile) -> App:
    config = build_app_config(
        version=version,
        app_name="Big Button",
        app_alias="big-button",
        platform=platform,
        app_id=app_id
    )
    return build_app(config=config)

