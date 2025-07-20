from src.configs.vehicle_config import VehicleConfig
from src.enums import VehicleType
from src.models import Model
from src.models.mass import Mass


class Vehicle(Model):
    config: VehicleConfig

    def __init__(self, config: VehicleConfig):
        super().__init__(name=config.name, config=config)

    @property
    def type(self) -> VehicleType:
        return self.config.type

    @property
    def mass(self) -> Mass:
        return self.config.mass

    def update(self):
        print("Vehicle update")

