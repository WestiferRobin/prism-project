from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.model_configs.drone_config import DroneConfig


class BotConfig(Config):
    drone: DroneConfig

    def __init__(self, drone: DroneConfig, **bot_data):
        super().__init__(
            version=drone.version,
            alias=drone.alias,
            name=drone.name,
            drone=drone,
            **bot_data
        )

    @property
    def id(self) -> UUID:
        return self.drone.id

    @property
    def name(self) -> str:
        return self.drone.name



