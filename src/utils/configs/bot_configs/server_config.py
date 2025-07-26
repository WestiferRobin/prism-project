from src.utils.configs.bot_configs import BotConfig
from src.utils.configs.drone_config import DroneConfig


class ServerConfig(BotConfig):
    def __init__(self, drone: DroneConfig):
        super().__init__(drone=drone)
