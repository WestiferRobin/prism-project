from src.api.builders.app_builders import build_app
from src.api.builders.app_builders.tool_builders import build_prism_lab
from utils.validators.app_validators import validate_lab
from src.utils.constants import DEBUG_VERSION
from src.utils.enums.platform_enums import PlatformType


def test_prism_lab(version: int = DEBUG_VERSION, platform: PlatformType = PlatformType.Web) -> None:
    prism_lab = build_prism_lab(
        version=version,
        platform=platform
    )
    expected_lab = build_app(config=prism_lab.config)
    validate_lab(
        lab=prism_lab,
        expected_app=expected_lab
    )

