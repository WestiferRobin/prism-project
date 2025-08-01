from src.utils.constants import DEV_VERSION
from src.utils.enums.platform_enums import PlatformType
from unit.test_apps.test_mobile_apps import test_prism_cook, test_prism_reflect
from unit.test_apps.test_solar_conquest import test_solar_conquest
from unit.test_apps.test_web_apps import test_prism_labs, test_prism_tables, test_prism_studio, test_prism_scribe, \
    test_prism_forge, test_prism_hive
from unit.test_net.test_bots import test_hedron_server, test_bot_drone, test_bot_speeder, test_bot_legion


def test_pc_games(version: int = DEV_VERSION) -> None:
    # only one game... when finished or team or studio we make videos
    test_solar_conquest(platform=PlatformType.PC, version=version)


def test_web_apps(version: int = DEV_VERSION) -> None:
    # stem-simulator: tool vs widget apps
    test_prism_labs(platform=PlatformType.Web, version=version, is_tool=True)
    test_prism_tables(platform=PlatformType.Web, version=version, is_tool=False)

    # media-generator: tool vs widget apps
    test_prism_studio(platform=PlatformType.Web, version=version)
    test_prism_scribe(platform=PlatformType.Web, version=version)

    # ai workflow: tool vs social/market/money apps
    test_prism_forge(platform=PlatformType.Web, version=version)
    test_prism_hive(platform=PlatformType.Web, version=version)


def test_mobile_apps(version: int = DEV_VERSION) -> None:
    # only mobile app specific
    test_prism_cook(platform=PlatformType.Mobile, version=version)
    test_prism_reflect(platform=PlatformType.Mobile, version=version)

    # only web apps
    test_prism_forge(platform=PlatformType.Mobile, version=version)
    test_prism_hive(platform=PlatformType.Mobile, version=version)

    # mobile_game is a mobile_app
    test_solar_conquest(platform=PlatformType.Mobile, version=version)


def test_bots(version: int = DEV_VERSION) -> None:
    test_hedron_server(version=version)
    test_bot_drone(version=version)
    test_bot_speeder(version=version)
    test_bot_legion(version=version)


def test_platform(version: int = DEV_VERSION):
    test_pc_games(version=version)
    test_web_apps(version=version)
    test_mobile_apps(version=version)
    test_bots(version=version)

