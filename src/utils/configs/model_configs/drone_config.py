from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.model_configs.prism_config import PrismConfig


class DroneConfig(Config):
    prism_config: PrismConfig

    def __init__(self, prism_config: PrismConfig, **prism_data):
        super().__init__(
            version=prism_config.version,
            config_id=prism_config.id,
            name=prism_config.name,
            alias=prism_config.alias,
            prism_config=prism_config,
            **prism_data
        )

