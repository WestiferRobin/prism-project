from utils.validators.config_validators.bot_configs import validate_bot_config
from src.models.drones import Drone
from src.models.drones.bot_drone import BotDrone
from src.utils.configs.bot_configs import BotConfig


def validate_bot_drone(bot: BotDrone) -> None:
    assert bot is not None
    assert isinstance(bot, BotDrone)
    assert isinstance(bot, Drone)

    assert bot.config is not None
    assert isinstance(bot.config, BotConfig)
    validate_bot_config(config=bot.config)


    validate_drone(drone=bot)
