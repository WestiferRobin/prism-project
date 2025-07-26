from src.platform import Platform
from src.utils.enums.platform_enums import PlatformType


def build_platform(platform_type: PlatformType) -> Platform:
    return Platform(type=platform_type)

