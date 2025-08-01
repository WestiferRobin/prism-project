from typing import List
from uuid import UUID

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.model_configs.user_config import UserConfig


class GameConfig(AppConfig):
    def __init__(self, game_id: UUID, **game_data) -> None:
        super().__init__(app_id=game_id, app_data=game_data)

    @property
    def player_configs(self) -> List[UserConfig]:
        return self.user_configs

