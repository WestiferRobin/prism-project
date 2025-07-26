from src.utils.configs.bot_configs import BotConfig
from src.utils.configs.model_configs.drone_config import DroneConfig


class ServerConfig(BotConfig):
    def __init__(self, drone: DroneConfig, **server_data):
        super().__init__(drone=drone, **server_data)
