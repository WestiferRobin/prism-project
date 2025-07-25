from src.utils.constants import CURRENT_VERSION


def test_pc_apps():
    pc_platform = build_platform(platform_type=PlatformType.PC)

    pc_platform.load_app(build_prism_forge())
    pc_platform.load_app(build_prism_studio())
    pc_platform.load_app(build_solar_conquest())

    validate_platform(pc_platform)


def test_web_apps():
    web_platform = build_platform(platform_type=PlatformType.Web)

    web_platform.load_app(build_prism_hive())
    web_platform.load_app(build_prism_studio())
    web_platform.load_app(build_prism_forge())

    validate_platform(web_platform)


def test_mobile_apps():
    web_platform = build_platform(platform_type=PlatformType.Mobile)

    web_platform.load_app(build_prism_hive())
    web_platform.load_app(build_prism_studio())
    web_platform.load_app(build_prism_forge())

    validate_platform(web_platform)


def test_iot_apps():
    web_platform = build_platform(platform_type=PlatformType.Mobile)

    web_platform.load_app(build_drone_bot())
    web_platform.load_app(build_legion_speeder())
    web_platform.load_app(build_arch_legion())

    validate_platform(web_platform)


def test_platform():
    test_pc_apps()
    test_web_apps()
    test_mobile_apps()
    test_iot_apps()
