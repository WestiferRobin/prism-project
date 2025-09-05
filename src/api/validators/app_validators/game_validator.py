from src.api.builders.app_builders.game_builder import build_game
from src.api.validators.app_validators import validate_app
from src.api.validators.config_validators import validate_app_config
from src.models.app.game import Game
from src.utils.configs.app_configs.game_config import GameConfig


def validate_game(source_game: Game, target_game: Game) -> None:
    assert type(source_game) == Game
    assert type(source_game.game_config) == GameConfig
    validate_app_config(
        source_config=source_game.game_config,
        target_config=source_game.app_config
    )
    validate_game_config()

    validate_app(source_app=source_game, target_app=)


def validate_solar_conquest(solar_conquest: Game) -> None:
    target = build_game(config=solar_conquest.game_config)
    validate_game(source_game=solar_conquest, target_game=target)

