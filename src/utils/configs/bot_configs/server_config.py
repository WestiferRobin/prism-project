from src.utils.configs.bot_configs import BotConfig
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.user_config import UserConfig


class ServerConfig(BotConfig):
    owner_config: UserConfig

    @property
    def companion_config(self) -> DroneConfig:
        return self.drone_config

    def __init__(self,
        owner_config: UserConfig,
        companion_config: DroneConfig,
        **server_data
    ):
        super().__init__(
            owner_config=owner_config,
            owner_id=owner_config.id,
            drone_config=companion_config,
            bot_data=server_data
        )
