from src.models.vehicles.speeders import Speeder
from src.utils.configs.model_configs.vehicle_configs.speeder_config import SpeederConfig


class BotSpeeder(Speeder):
    def __init__(self, config: SpeederConfig, **speeder_data):
        super().__init__(
            config=config,
            speeder_data=speeder_data
        )

