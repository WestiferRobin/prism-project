from src.models.drones import Drone
from src.utils.configs.bot_configs import BotConfig


class BotDrone(Drone):
    bot_config: BotConfig

    def __init__(self, config: BotConfig):
        super().__init__(
            bot_config=config,
            config=config.drone
        )

