from uuid import UUID

from src.utils.configs.model_configs.drone_config import DroneConfig


class BotConfig(DroneConfig):
    bot_id: UUID

    def __init__(self, config: DroneConfig, bot_id: UUID = None, **bot_data):
        if bot_id is None:
            bot_id = config.id
        super().__init__(
            prism_config=config.prism_config,
            bot_id=bot_id,
            **bot_data
        )

