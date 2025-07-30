from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.prism_config import PrismConfig


class BotConfig(Config):
    drone_config: DroneConfig

    def __init__(self, owner_id: UUID, drone_config: DroneConfig, **bot_data):
        super().__init__(config_id=owner_id, drone_config=drone_config, **bot_data)

    @property
    def owner_id(self) -> UUID:
        return self.id

    @property
    def prism_config(self) -> PrismConfig:
        return self.drone_config.prism_config

    @property
    def avatar_config(self) -> DroneConfig:
        return self.owner_config.avatar_config

