from src.api.validators.drone_validator import validate_drone
from src.app.bot import Bot
from src.utils.configs.bot_config import BotConfig


def validate_bot(bot: Bot) -> None:
    assert isinstance(bot, Bot)
    assert isinstance(bot.config, BotConfig)

    validate_drone(bot.drone)

