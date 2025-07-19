from src.enums import VehicleType
from src.configs import Config


class VehicleConfig(Config):
    type: VehicleType

    def __init__(self, vehicle_type: VehicleType):
        super().__init__(name=vehicle_type.name, type=vehicle_type)


class SpeederConfig(VehicleConfig):
    def __init__(self):
        super().__init__(VehicleType.Speeder)


class ShuttleConfig(VehicleConfig):
    def __init__(self):
        super().__init__(VehicleType.Shuttle)

