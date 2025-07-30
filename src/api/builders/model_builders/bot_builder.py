from src.models.drones.bot_drone import BotDrone
from src.models.hive_server import HedronServer
from src.utils.configs.bot_configs import BotConfig
from src.utils.configs.bot_configs.server_config import ServerConfig


def build_hedron_server(config: ServerConfig) -> HedronServer:
    return HedronServer(config=config)


def build_bot_drone(config: BotConfig) -> BotDrone:
    return BotDrone(config=config)

