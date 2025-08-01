from pydantic import BaseModel

from src.models.drones import Drone
from src.utils.configs.model_configs.user_config import UserConfig


class User(BaseModel):
    config: UserConfig

    def __init__(self, **user_data):
        super().__init__(**user_data)

    @property
    def avatar(self) -> Drone:
        return Drone(config=self.config.avatar_config)

