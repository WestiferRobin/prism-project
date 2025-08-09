from typing import List
from uuid import UUID, uuid4

from src.api.builders.config_builders.app_configs import build_game_config
from src.app.game import Game
from src.models.controllers.faction_controller import FactionController
from src.models.legion.faction import Faction
from src.utils.configs.app_configs.game_config import GameConfig
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.enums.game_enums import GameMode
from src.utils.enums.platform_enums import PlatformType


def build_game_controller(
    player_config: UserConfig,
    player_faction: Faction,
) -> FactionController:
    return FactionController(
        player_config=player_config,
        player_faction=player_faction
    )


def build_game(config: GameConfig) -> Game:
    return Game(config=config)


def build_solar_conquest(
    version: int = 0,
    game_id: UUID = None,
    game_mode: GameMode = GameMode.Classic,
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
        game_mode=game_mode,
        platform=platform,
        player_configs=account_configs
    )

    solar_conquest = build_game(config=game_config)
    return solar_conquest

