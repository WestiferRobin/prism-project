from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.config_builders.account_configs import build_account_config
from src.api.builders.config_builders.user_configs.max_config import build_max_config
from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.api.validators.app_validators.game_validator import validate_solar_conquest
from src.utils.constants import DEBUG_VERSION, MVP_VERSIONS
from src.utils.enums.game_enums import GameMode
from src.utils.enums.platform_enums import PlatformType


def test_solar_conquest_classic(
    version: int = DEBUG_VERSION,
    platform: PlatformType=PlatformType.PC,
):
    solar_conquest = build_solar_conquest(
        version=version,
        game_mode=GameMode.Classic,
        platform=platform,
    )
    wes_config = build_wes_config(version=version)
    max_config = build_max_config(version=version)
    account_configs = [
        build_account_config(
            version=version,
            user_id=wes_config.user_id,
            app_name=solar_conquest.app_name,
            app_alias=solar_conquest.app_alias,
        ),
        build_account_config(
            version=version,
            user_id=wes_config.user_id,
            app_name=solar_conquest.app_name,
            app_alias=solar_conquest.app_alias,
        ),
    ]
    validate_solar_conquest(solar_conquest=solar_conquest)


def test_solar_conquest_campaign(
    version: int = DEBUG_VERSION,
    platform: PlatformType=PlatformType.PC,
):
    wes_config = build_wes_config(version=version)
    solar_conquest = build_solar_conquest(version=version, game_mode=GameMode.Campaign, platform=platform)
    validate_solar_conquest(solar_conquest=solar_conquest)


def test_solar_conquest_royale(
    version: int = DEBUG_VERSION,
    platform: PlatformType=PlatformType.PC,
):
    solar_conquest = build_solar_conquest(version=version, game_mode=GameMode.Royale, platform=platform)
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




