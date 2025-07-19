from src.configs.vehicle_config import VehicleConfig, SpeederConfig, ShuttleConfig
from src.enums.vehicle_enums import VehicleType
from src.models import Model
from src.models.unit import Mass


class Vehicle(Model):
    config: VehicleConfig

    def __init__(self, config: VehicleConfig):
        super().__init__(name=config.name, config=config)

    @property
    def type(self) -> VehicleType:
        return self.config.type

    @property
    def mass(self) -> Mass:
        return Mass(amount=self.config.mass_amount)

    def update(self):
        print("Vehicle update")


class Speeder(Vehicle):
    def __init__(self, mass_amount: float):
        config = SpeederConfig(mass_amount=mass_amount)
        super().__init__(config)

    def update(self):
        print("Speeder update")


class Shuttle(Vehicle):
    def __init__(self, mass_amount: float):
        config = ShuttleConfig(mass_amount=mass_amount)
        super().__init__(config)

    def update(self):
        print("Shuttle update")