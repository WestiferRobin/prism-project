from src.api.builders import build_prism_lab, build_prism_studio, build_prism_forge, build_prism_hive
from src.utils.constants import LAMBDA_VERSION
from src.utils.enums.platform_enums import PlatformType


def test_prism_labs(platform: PlatformType = PlatformType.Web, version: int = LAMBDA_VERSION) -> None:
    prism_labs = build_prism_lab(platform=platform, version=version)
    validate_labs(labs=prism_labs, expected_platform=platform, expected_version=version)


def test_prism_studio(platform: PlatformType = PlatformType.Web, version: int = LAMBDA_VERSION) -> None:
    prism_studio = build_prism_studio(platform=platform, version=version)
    validate_studio(studio=prism_studio, expected_platform=platform, expected_version=version)


def test_prism_tables(platform: PlatformType = PlatformType.Web, version: int = LAMBDA_VERSION) -> None:
    prism_tables = build_prism_tables(platform=platform, version=version)
    validate_tables(tables=prism_tables, expected_platform=platform, expected_version=version)


def test_prism_scribe(platform: PlatformType = PlatformType.Web, version: int = LAMBDA_VERSION) -> None:
    prism_scribe = build_prism_scribe(platform=platform, version=version)
    validate_scribe(scribe=prism_scribe, expected_platform=platform, expected_version=version)


def test_prism_forge(platform: PlatformType = PlatformType.Web, version: int = LAMBDA_VERSION) -> None:
    prism_forge = build_prism_forge(platform=platform, version=version)
    validate_forge(forge=prism_forge, expected_platform=platform, expected_version=version)


def test_prism_hive(platform: PlatformType = PlatformType.Web, version: int = LAMBDA_VERSION) -> None:
    prism_hive = build_prism_hive(platform=platform, version=version)
    validate_hive(hive=prism_hive, expected_platform=platform, expected_version=version)

