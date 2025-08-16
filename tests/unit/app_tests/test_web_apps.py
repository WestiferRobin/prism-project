from src.api.builders.app_builders import build_prism_hive, build_app
from src.api.builders.app_builders.tool_builders import build_prism_lab, build_prism_studio, build_prism_forge
from utils.validators.app_validators import validate_lab, validate_studio, validate_forge, validate_hive
from src.utils.constants import DEV_VERSION
from src.utils.enums.platform_enums import PlatformType



def test_prism_labs(platform: PlatformType = PlatformType.Web, version: int = DEV_VERSION) -> None:
    prism_labs = build_prism_lab(platform=platform, version=version)
    expected_app = build_app(config=prism_labs.config)
    validate_lab(lab=prism_labs, expected_app=expected_app)


def test_prism_studio(platform: PlatformType = PlatformType.Web, version: int = DEV_VERSION) -> None:
    prism_studio = build_prism_studio(platform=platform, version=version)
    expected_app = build_app(config=prism_studio.config)
    validate_studio(studio=prism_studio, expected_app=expected_app)


def test_prism_forge(platform: PlatformType = PlatformType.Web, version: int = DEV_VERSION) -> None:
    prism_forge = build_prism_forge(platform=platform, version=version)
    expected_app = build_app(config=prism_forge.config)
    validate_forge(forge=prism_forge, expected_app=expected_app)


def test_prism_hive(platform: PlatformType = PlatformType.Web, version: int = DEV_VERSION) -> None:
    prism_hive = build_prism_hive(platform=platform, version=version)
    expected_app = build_app(config=prism_hive.config)
    validate_hive(hive=prism_hive, expected_app=expected_app)

