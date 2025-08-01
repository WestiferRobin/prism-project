from typing import Dict, List
from uuid import UUID

from src.api.builders.app_builders import build_prism_cook, build_prism_hive, build_big_button
from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.app_builders.mobile_apps.prism_reflect import build_prism_reflect
from src.api.builders.app_builders.tool_builders import build_prism_forge, build_prism_lab, build_prism_studio
from src.app import App
from src.utils.constants import DEV_VERSION, TEST_VERSION, PROD_VERSION, ALPHA_VERSION, BETA_VERSION, FINAL_VERSION
from src.utils.constants.user_constants import WES_ID, EMMA_ID, MAX_ID, MARY_ID, TYLER_ID, PAYTON_ID, BRIAN_ID
from src.utils.enums.platform_enums import PlatformType


def configure_app_registry(version: int) -> Dict[UUID, List[App]]:
    wes_apps = []
    emma_apps = []
    mary_apps = []
    max_apps = []

    if version >= DEV_VERSION:
        wes_apps.append(build_prism_lab(version=version, platform=PlatformType.Web))
        emma_apps.append(build_prism_cook(version=version, platform=PlatformType.Mobile))
        mary_apps.append(build_prism_studio(version=version, platform=PlatformType.Web))
        max_apps.append(build_solar_conquest(version=version, platform=PlatformType.Mobile))
    if version >= TEST_VERSION:
        wes_apps.append(build_solar_conquest(version=version, platform=PlatformType.PC))
        emma_apps.append(build_prism_lab(version=version))
        mary_apps.append(build_prism_cook(version=version))
        max_apps.append(build_prism_studio(version=version))
    if version >= PROD_VERSION:
        wes_apps.append(build_prism_forge(version=version))
        emma_apps.append(build_prism_forge(version=version))
        mary_apps.append(build_prism_forge(version=version))
        max_apps.append(build_prism_forge(version=version))

    tyler_apps = []
    payton_apps = []
    brian_apps = []

    if version >= ALPHA_VERSION:
        wes_apps.append(build_prism_hive(version=version))
        emma_apps.append(build_prism_hive(version=version))
        mary_apps.append(build_prism_hive(version=version))
        max_apps.append(build_prism_hive(version=version))

        tyler_apps.append(build_prism_forge(version=version))
        payton_apps.append(build_prism_forge(version=version))
        brian_apps.append(build_prism_forge(version=version))
    if version >= BETA_VERSION:
        wes_apps.append(build_prism_reflect(version=version))
        emma_apps.append(build_big_button(version=version))
        mary_apps.append(build_big_button(version=version))
        max_apps.append(build_big_button(version=version))

        tyler_apps.append(build_big_button(version=version))
        payton_apps.append(build_big_button(version=version))
        brian_apps.append(build_prism_lab(version=version))
    if version >= FINAL_VERSION:
        wes_apps.append(build_solar_conquest(version=version, platform=PlatformType.Mobile))
        emma_apps.append(build_solar_conquest(version=version))
        mary_apps.append(build_solar_conquest(version=version))
        max_apps.append(build_solar_conquest(version=version))

        tyler_apps.append(build_solar_conquest(version=version))
        payton_apps.append(build_solar_conquest(version=version))
        brian_apps.append(build_solar_conquest(version=version))



    registry = {
        WES_ID: wes_apps,
        EMMA_ID: emma_apps,
        MARY_ID: mary_apps,
        MAX_ID: max_apps,

        TYLER_ID: tyler_apps,
        PAYTON_ID: payton_apps,
        BRIAN_ID: brian_apps,
    }

    return registry

