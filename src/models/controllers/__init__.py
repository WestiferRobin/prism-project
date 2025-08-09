from pydantic import BaseModel

from src.utils.configs.model_configs.user_config import UserConfig


class Controller(BaseModel):
    player_config: UserConfig

