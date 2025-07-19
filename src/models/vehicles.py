from pydantic import BaseModel

from src.configs.vehicle_config import VehicleConfig, SpeederConfig, ShuttleConfig
from src.enums.vehicle_enums import VehicleType


class Vehicle(BaseModel):
    config: VehicleConfig

    def __init__(self, config: VehicleConfig):
        super().__init__(config=config)

    @property
    def type(self) -> VehicleType:
        return self.config.type

    @property
    def name(self):
        return self.type.name


class Speeder(Vehicle):
    def __init__(self):
        super().__init__(SpeederConfig())


class Shuttle(Vehicle):
    def __init__(self):
        super().__init__(ShuttleConfig())

