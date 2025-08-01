from src.api.builders import build_prism_reflect
from src.utils.enums.platform_enums import PlatformType


def test_prism_cook(platform: PlatformType = PlatformType.Web, version: int = 1) -> None:
    prism_cook = build_prism_cook(platform=platform, version=version)
    validate_cook(cook=prism_cook, version=version)


def test_prism_reflect(platform: PlatformType = PlatformType.Web, version: int = 1) -> None:
    prism_reflect = build_prism_reflect(platform=platform, version=version)
    validate_reflect(reflect=prism_reflect, version=version)

