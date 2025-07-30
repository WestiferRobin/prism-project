from src.api.validators.app_validators import validate_app
from src.app.game import Game


def validate_game(game: Game) -> None:
    assert isinstance(game, Game)

    validate_app(app=game, expected_platform=game.platform)


def validate_solar_conquest(game: Game) -> None:
    validate_game(game=game)

