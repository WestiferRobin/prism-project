import uuid
from typing import List
from uuid import UUID

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.enums.game_enums import GameMode


class GameConfig(AppConfig):
    mode: GameMode

    def __init__(self,
        game_id: UUID,
        player_configs: List[AccountConfig],
        **game_data
    ) -> None:
        super().__init__(
            app_id=game_id,
            account_configs=player_configs,
            **game_data
        )

    @property
    def player_configs(self) -> List[UserConfig]:
        return self.user_configs


class ClassicConfig(GameConfig):
    def __init__(self,
        player_config: AccountConfig,
        enemy_config: AccountConfig,
        game_id: UUID = None
    ):
        if game_id is None:
            game_id = uuid.uuid4()
        super().__init__(
            game_id=game_id,
            game_mode=GameMode.Classic,
            player_configs=[player_config, enemy_config]
        )


class CampaignConfig(GameConfig):
    def __init__(self,
        federation_config: AccountConfig,
        empire_config: AccountConfig,
    ):
        pass

