from typing import List
from uuid import UUID, uuid4

from src.api.builders.config_builders.app_configs import build_game_config
from src.app.game import Game
from src.utils.configs.app_configs.game_config import GameConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.enums.platform_enums import PlatformType
from src.utils.user import User


def build_game(
    version: int,
    game_name: str,
    game_alias: str,
    platform: PlatformType,
    game_id: UUID = None,
) -> Game:
    if game_id is None:
        game_id = uuid4()
    game_config = build_game_config(
        version=version,
        game_name=game_name,
        game_alias=game_alias,
        platform=platform,
        game_id=game_id,
    )
    return Game(config=game_config)


def build_solar_conquest(
    version: int = 0,
    game_id: UUID = None,
    platform: PlatformType = PlatformType.PC,
    player_configs: List[UserConfig] = None
) -> Game:
    if game_id is None:
        game_id = uuid4()
    if player_configs is None:
        player_configs = []
    game_config = build_game_config(
        version=version,
        game_id=game_id,
        game_name="Solar Conquest",
        game_alias="solar-conquest",
        platform=platform,
        player_configs=player_configs
    )

    solar_conquest = build_game(config=game_config)
    return solar_conquest

