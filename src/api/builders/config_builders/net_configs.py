from typing import List
from uuid import UUID, uuid4

from src.utils.configs.app_configs import AppConfig
from src.utils.configs.bot_configs import BotConfig
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.configs.net_config import NetConfig


def build_net_config(
    version: int,
    user_configs: List[UserConfig],
    app_configs: List[AppConfig],
    bot_configs: List[BotConfig],
    net_id: UUID = None
) -> NetConfig:
    if net_id is None:
        net_id = uuid4()
    return NetConfig(
        version=version,
        user_configs=user_configs,
        app_configs=app_configs,
        bot_configs=bot_configs,
        config_id=net_id,
    )

