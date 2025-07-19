from src.configs.vehicle_config import VehicleConfig
from src.enums import VehicleType
from src.models.vehicles import Speeder, Shuttle, Vehicle


def build_vehicle(vehicle_type: VehicleType, mass_amount: float) -> Vehicle:
    config = VehicleConfig(vehicle_type=vehicle_type, mass_amount=mass_amount)
    return Vehicle(config=config)


def build_speeder(mass_amount: float) -> Speeder:
    return Speeder(mass_amount=mass_amount)


def build_shuttle(mass_amount: float) -> Shuttle:
    return Shuttle(mass_amount=mass_amount)

