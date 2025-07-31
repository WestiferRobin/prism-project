import uuid
from typing import cast
from uuid import UUID

from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.prism_config import PrismConfig


class UserConfig(PrismConfig):
    def __init__(self, user_id: UUID, **prism_data):
        super().__init__(
            config_id=user_id,
            **prism_data
        )

    @property
    def avatar_config(self) -> DroneConfig:
        return cast(DroneConfig, self)
