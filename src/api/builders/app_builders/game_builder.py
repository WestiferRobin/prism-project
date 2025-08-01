from typing import List
from uuid import UUID, uuid4

from src.api.builders.config_builders.app_configs import build_game_config
from src.app.game import Game
from src.utils.configs.app_configs.game_config import GameConfig
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.enums.platform_enums import PlatformType


def build_game(config: GameConfig) -> Game:
    return Game(config=config)


def build_solar_conquest(
    version: int = 0,
    game_id: UUID = None,
    platform: PlatformType = PlatformType.PC,
    account_configs: List[AccountConfig] = None
) -> Game:
    if game_id is None:
        game_id = uuid4()
    if account_configs is None:
        account_configs = []
    game_config = build_game_config(
        version=version,
        game_id=game_id,
        game_name="Solar Conquest",
        game_alias="solar-conquest",
        platform=platform,
        player_configs=account_configs
    )

    solar_conquest = build_game(config=game_config)
    return solar_conquest

