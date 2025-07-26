from src.api.builders.app_builders.game_builder import build_solar_conquest
from zlegacy.api.validators import validate_solar_conquest


def test_solar_conquest():
    solar_conquest = build_solar_conquest()
    validate_solar_conquest(solar_conquest)

