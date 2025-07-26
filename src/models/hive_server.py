from pydantic import BaseModel

from src.models.drones import Drone
from src.utils.configs.bot_configs.server_config import ServerConfig


class HiveServer(BaseModel):
    config: ServerConfig

    @property
    def drone(self) -> Drone:
        return Drone(config=self.config.drone)

