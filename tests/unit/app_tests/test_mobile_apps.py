from src.api.builders import build_prism_reflect
from src.utils.constants import DEV_VERSION
from src.utils.enums.platform_enums import PlatformType


def test_prism_cook(platform: PlatformType = PlatformType.Web, version: int = DEV_VERSION) -> None:
    prism_cook = build_prism_cook(platform=platform, version=version)
    validate_cook(cook=prism_cook, version=version)


def test_prism_reflect(platform: PlatformType = PlatformType.Web, version: int = DEV_VERSION) -> None:
    prism_reflect = build_prism_reflect(platform=platform, version=version)
    validate_reflect(reflect=prism_reflect, version=version)


def test_prism_tables(version: int = DEV_VERSION, is_forge_widget: bool = False) -> None:
    if is_forge_widget:
        platform = PlatformType.Web
    else:
        platform = PlatformType.Mobile
    prism_tables = build_prism_tables(platform=platform, version=version)
    validate_tables(tables=prism_tables, expected_platform=platform, expected_version=version)


def test_prism_scribe(platform: PlatformType = PlatformType.Web, version: int = DEV_VERSION) -> None:
    prism_scribe = build_prism_scribe(platform=platform, version=version)
    validate_scribe(scribe=prism_scribe, expected_platform=platform, expected_version=version)

