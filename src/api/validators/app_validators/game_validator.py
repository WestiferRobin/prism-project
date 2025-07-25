from src.api.validators.app_validators import validate_app
from src.app.game import Game


def validate_game(game: Game) -> None:
    assert isinstance(game, Game)
    validate_app(game)

