from src.models.vehicles import Vehicle
from src.utils.configs.model_configs.vehicle_configs.speeder_config import SpeederConfig


class Speeder(Vehicle):
    def __init__(self, config: SpeederConfig, **speeder_data):
        super().__init__(config=config, vehicle_data=speeder_data)

    def update(self):
        print("Speeder update")

