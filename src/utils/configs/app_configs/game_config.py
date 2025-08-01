from typing import List
from uuid import UUID

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.account_config import AccountConfig
from src.utils.configs.model_configs.user_config import UserConfig


class GameConfig(AppConfig):
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

