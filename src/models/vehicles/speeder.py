from src.configs.vehicle_config import VehicleConfig
from src.models.vehicles import Vehicle


class Speeder(Vehicle):
    def __init__(self, config: VehicleConfig):
        super().__init__(config)

    def update(self):
        print("Speeder update")

