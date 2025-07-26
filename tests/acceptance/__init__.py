from src.api.builders.app_builders import build_prism_hive
from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.app_builders.iot_builder import build_hedron_bot, build_hive_server, build_avatar_legion
from src.api.builders.app_builders.tool_builders import build_prism_reflect, build_prism_forge, build_prism_studio, \
    build_prism_lab
from src.api.builders.platform_builder import build_platform
from src.api.validators.platform_validator import validate_platform
from src.utils.enums.platform_enums import PlatformType


def test_pc_apps():
    pc_platform = build_platform(platform_type=PlatformType.PC)

    pc_platform.load_app(app=build_solar_conquest(platform=PlatformType.PC))
    pc_platform.load_app(app=build_prism_studio(platform=PlatformType.PC))
    pc_platform.load_app(app=build_prism_lab(platform=PlatformType.PC))
    pc_platform.load_app(app=build_prism_forge(platform=PlatformType.PC))

    validate_platform(platform=pc_platform, expected_type=PlatformType.PC)


def test_web_apps():
    web_platform = build_platform(platform_type=PlatformType.Web)

    web_platform.load_app(app=build_prism_lab())
    web_platform.load_app(app=build_prism_studio())
    web_platform.load_app(app=build_prism_forge())
    web_platform.load_app(app=build_prism_hive(platform=PlatformType.Web))

    validate_platform(platform=web_platform, expected_type=PlatformType.Web)


def test_mobile_apps():
    mobile_platform = build_platform(platform_type=PlatformType.Mobile)

    mobile_platform.load_app(app=build_prism_reflect())
    mobile_platform.load_app(app=build_solar_conquest(platform=PlatformType.Mobile))
    mobile_platform.load_app(app=build_prism_hive(platform=PlatformType.Mobile))
    mobile_platform.load_app(app=build_prism_studio(platform=PlatformType.Mobile))

    validate_platform(platform=mobile_platform, expected_type=PlatformType.Mobile)


def test_iot_apps():
    iot_platform = build_platform(platform_type=PlatformType.Iot)

    iot_platform.load_app(app=build_hive_server())
    iot_platform.load_app(app=build_hedron_bot())
    iot_platform.load_app(app=build_avatar_legion())

    validate_platform(platform=iot_platform, expected_type=PlatformType.Iot)


def test_platform():
    test_pc_apps()
    test_web_apps()
    test_mobile_apps()
    test_iot_apps()
