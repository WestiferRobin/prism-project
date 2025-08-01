from pydantic import BaseModel

from src.utils.configs.bot_configs import BotConfig


class Bot(BaseModel):
    config: BotConfig

