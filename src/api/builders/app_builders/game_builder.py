from src.api.builders.config_builders.app_configs import build_game_config
from src.api.builders.config_builders.user_configs import build_wes_config, build_max_config
from src.app.game import Game
from src.utils.configs.app_configs.game_config import GameConfig
from src.utils.enums.platform_enums import PlatformType


def build_game(config: GameConfig) -> Game:
    return Game(config=config)


def build_solar_conquest(platform: PlatformType = PlatformType.PC, version: int = 0) -> Game:
    game_config = build_game_config(name="Solar Conquest", platform=platform)

    players = [ build_wes_config() ]
    if version >= 1:
        players.append(build_max_config())

    solar_conquest = build_game(config=game_config)
    return solar_conquest

