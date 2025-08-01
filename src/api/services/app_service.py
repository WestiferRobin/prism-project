from typing import List

from src.api.builders.app_builders import build_app_list, build_prism_cook, build_prism_hive
from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.app_builders.tool_builders import build_prism_lab, build_prism_forge, build_prism_studio
from src.app import App
from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants import DEV_VERSION, TEST_VERSION, PROD_VERSION, ALPHA_VERSION, FINAL_VERSION, \
    BETA_VERSION


def get_app_configs(version: int) -> List[AppConfig]:
    app_configs = []

    if version >= DEV_VERSION:
        app_configs.append(build_solar_conquest(version=version))
    if version >= TEST_VERSION:
        app_configs.append(build_prism_cook(version=version))
    if version >= PROD_VERSION:
        app_configs.append(build_prism_lab(version=version))
    if version >= ALPHA_VERSION:
        app_configs.append(build_prism_studio(version=version))
    if version >= BETA_VERSION:
        app_configs.append(build_prism_forge(version=version))
    if version >= FINAL_VERSION:
        app_configs.append(build_prism_hive(version=version))

    return app_configs


def get_apps(version: int, user_configs: List[UserConfig]) -> List[App]:
    app_configs = get_app_configs(version)
    app_list = build_app_list(configs=app_configs)
    return app_list
