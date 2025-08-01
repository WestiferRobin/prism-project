from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.validators.app_validators.game_validator import validate_solar_conquest
from src.utils.constants import DEV_VERSION, DEBUG_VERSION, MVP_VERSIONS
from src.utils.enums.game_enums import GameMode
from src.utils.enums.platform_enums import PlatformType


def test_solar_conquest_classic(
    version: int = DEBUG_VERSION,
    platform: PlatformType=PlatformType.PC,
):
    solar_conquest = build_solar_conquest(
        version=version,
        platform=platform,
        mode=GameMode.Classic
    )
    validate_solar_conquest(solar_conquest=solar_conquest)


def test_solar_conquest_campaign(
    version: int = DEBUG_VERSION,
    platform: PlatformType=PlatformType.PC,
):
    solar_conquest = build_solar_conquest(
        version=version,
        platform=platform,
        mode=GameMode.Campaign
    )
    validate_solar_conquest(solar_conquest=solar_conquest)


def test_solar_conquest_royale(
    version: int = DEBUG_VERSION,
    platform: PlatformType=PlatformType.PC,
):
    solar_conquest = build_solar_conquest(
        version=version,
        platform=platform,
        mode=GameMode.Royale
    )
    validate_solar_conquest(solar_conquest=solar_conquest)


def test_solar_conquest_pc_platform(version: int = DEBUG_VERSION):
    test_solar_conquest_classic(version=version, platform=PlatformType.PC)
    test_solar_conquest_campaign(version=version, platform=PlatformType.PC)
    test_solar_conquest_royale(version=version, platform=PlatformType.PC)


def test_solar_conquest_mobile_platform(version: int = DEBUG_VERSION):
    test_solar_conquest_classic(version=version, platform=PlatformType.Mobile)
    test_solar_conquest_campaign(version=version, platform=PlatformType.Mobile)
    test_solar_conquest_royale(version=version, platform=PlatformType.Mobile)


def test_solar_conquest_versions():
    for mvp_version in MVP_VERSIONS:
        test_solar_conquest_pc_platform(version=mvp_version)
        test_solar_conquest_mobile_platform(version=mvp_version)




