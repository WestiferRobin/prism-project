from src.models.drones.bot_drone import BotDrone
from src.utils.configs.bot_configs import BotConfig


def build_bot_drone(config: BotConfig) -> BotDrone:
    return BotDrone(config=config)

