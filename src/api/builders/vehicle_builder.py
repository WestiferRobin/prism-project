from src.configs.vehicle_config import VehicleConfig
from src.enums import VehicleType
from src.models.vehicles import Speeder, Shuttle, Vehicle


def build_vehicle(vehicle_type: VehicleType) -> Vehicle:
    config = VehicleConfig(vehicle_type=vehicle_type)
    return Vehicle(config=config)


def build_speeder() -> Speeder:
    return Speeder()


def build_shuttle() -> Shuttle:
    return Shuttle()

