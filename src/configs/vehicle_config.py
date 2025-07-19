from src.enums import VehicleType
from src.configs import Config


class VehicleConfig(Config):
    type: VehicleType
    mass_amount: float

    def __init__(self, vehicle_type: VehicleType, mass_amount: float):
        super().__init__(
            name=vehicle_type.name,
            type=vehicle_type,
            mass_amount=mass_amount
        )


class SpeederConfig(VehicleConfig):
    def __init__(self, mass_amount: float):
        super().__init__(VehicleType.Speeder, mass_amount)


class ShuttleConfig(VehicleConfig):
    def __init__(self, mass_amount: float):
        super().__init__(VehicleType.Shuttle, mass_amount)

