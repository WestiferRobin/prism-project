from typing import List

from src.api.builders.app_builders.game_builder import build_solar_conquest
from src.api.builders.config_builders.user_configs.max_config import build_max_config
from src.api.builders.config_builders.user_configs.tyler_config import build_tyler_config
from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.constants import DEBUG_VERSION
from src.utils.enums.game_enums import GameMode
from src.utils.enums.game_enums.faction_enums import FactionType


def configure_game_accounts(version: int, game_mode: GameMode) -> List[AccountConfig]:
    user_configs = []

    if game_mode == GameMode.Campaign:
        user_configs.append(build_wes_config(version=version))
    if game_mode == GameMode.Skirmish:
        user_configs.append(build_wes_config(version=version))
        user_configs.append(build_max_config(version=version))
    if game_mode == GameMode.Classic:
        user_configs.append(build_wes_config(version=version))
        user_configs.append(build_max_config(version=version))
    if game_mode == GameMode.Royale:
        user_configs.append(build_wes_config(version=version))
        user_configs.append(build_max_config(version=version))

    return [convert_user_to_account_configs]





def test_solar_conquest(version: int = DEBUG_VERSION):

    for game_mode in GameMode:
        game_accounts = configure_game_accounts(game_mode=game_mode)
        solar_conquest = build_solar_conquest(
            version=version,
            game_mode=game_mode,
            account_configs=game_accounts
        )

    # solar_conquest = build_solar_conquest(version=version)
    # expected_game = build_game(config=solar_conquest.game_config)
    # validate_campaign_game(game=solar_conquest, )
