from src.models.vehicles import Vehicle
from src.utils.configs.model_configs.vehicle_config import VehicleConfig
from src.utils.enums.vehicle_enums import VehicleType


class Speeder(Vehicle):
    def __init__(self, config: VehicleConfig):
        config.type = VehicleType.Speeder
        super().__init__(config)

    def update(self):
        print("Speeder update")

