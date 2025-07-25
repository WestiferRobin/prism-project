from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.prism_config import PrismConfig


class DroneConfig(Config):
    prism: PrismConfig

    @property
    def id(self) -> UUID:
        return self.prism.id

