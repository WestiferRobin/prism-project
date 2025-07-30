from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.validators.app_validators.game_validator import validate_solar_conquest
from src.utils.constants import INITIAL_VERSION
from src.utils.enums.platform_enums import PlatformType


def test_solar_conquest(platform: PlatformType=PlatformType.PC, version: int = INITIAL_VERSION):
    solar_conquest = build_solar_conquest(platform=platform, version=version)
    validate_solar_conquest(solar_conquest)

