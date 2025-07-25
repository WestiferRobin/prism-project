from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.drone_config import DroneConfig


class BotConfig(Config):
    drone: DroneConfig

    @property
    def id(self) -> UUID:
        return self.drone.id



