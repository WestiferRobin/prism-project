from src.platform import Platform
from src.utils.configs import Config
from src.utils.enums.platform_enums import PlatformType


def validate_platform(platform: Platform, expected_type: PlatformType) -> None:
    assert isinstance(platform, Platform)
    assert isinstance(platform.type, PlatformType)
    assert platform.type == expected_type
    assert isinstance(platform.config, Config)

