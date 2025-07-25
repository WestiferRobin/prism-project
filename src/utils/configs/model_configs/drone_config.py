from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.model_configs.prism_config import PrismConfig


class DroneConfig(Config):
    prism: PrismConfig

    def __init__(self, prism: PrismConfig, **prism_data):
        super().__init__(
            version=prism.version,
            name=prism.name,
            alias=prism.alias,
            prism=prism,
            **prism_data
        )

    @property
    def id(self) -> UUID:
        return self.prism.id

    @property
    def name(self) -> str:
        return self.prism.name

