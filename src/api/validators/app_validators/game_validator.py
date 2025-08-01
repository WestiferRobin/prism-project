from src.api.builders.app_builders.game_builder import build_game
from src.api.validators.app_validators import validate_app
from src.api.validators.config_validators import validate_config
from src.app.game import Game
from src.utils.configs.app_configs.game_config import GameConfig


def validate_game(source: Game, target: Game) -> None:
    assert type(source) == Game
    assert type(source.game_config) == GameConfig
    validate_config(
        source_config=source.game_config,
        target_config=source.app_config
    )
    validate_config(
        source_config=source.game_config,
        target_config=target.game_config,
    )

    validate_app(app=source, target_platform=source.platform)


def validate_solar_conquest(solar_conquest: Game) -> None:
    target = build_game(config=solar_conquest.game_config)
    validate_game(source=solar_conquest, target=target)

