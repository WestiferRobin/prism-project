from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.model_configs.prism_config import PrismConfig


class DroneConfig(Config):
    prism_config: PrismConfig

    def __init__(self, prism_config: PrismConfig, **prism_data):
        super().__init__(
            version=prism_config.version,
            name=prism_config.name,
            alias=prism_config.alias,
            prism=prism_config,
            **prism_data
        )

    @property
    def version(self) -> int:
        return self.prism_config.version

    @property
    def id(self) -> UUID:
        return self.prism_config.id

    @property
    def name(self) -> str:
        return self.prism_config.name

