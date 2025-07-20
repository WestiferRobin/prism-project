from src.configs.vehicle_config import VehicleConfig
from src.enums import VehicleType
from src.models.mass import Mass
from src.models.vehicles import Vehicle
from src.models.vehicles.shuttle import Shuttle
from src.models.vehicles.speeder import Speeder


def build_vehicle(vehicle_type: VehicleType, mass: Mass) -> Vehicle:
    config = VehicleConfig(vehicle_type=vehicle_type, mass=mass)
    return Vehicle(config=config)


def build_speeder(config: VehicleConfig) -> Speeder:
    return Speeder(config=config)


def build_shuttle(config: VehicleConfig) -> Shuttle:
    return Shuttle(config=config)

