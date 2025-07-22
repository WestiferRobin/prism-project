from app.configs.vehicle_config import VehicleConfig
from utils.enums import VehicleType
from app.models.equations.chemistry.mass import Mass
from app.models.vehicles import Vehicle
from app.models.vehicles.shuttle import Shuttle
from app.models.vehicles.speeder import Speeder


def build_vehicle(vehicle_type: VehicleType, mass: Mass) -> Vehicle:
    config = VehicleConfig(vehicle_type=vehicle_type, mass=mass)
    return Vehicle(config=config)


def build_speeder(config: VehicleConfig) -> Speeder:
    return Speeder(config=config)


def build_shuttle(config: VehicleConfig) -> Shuttle:
    return Shuttle(config=config)

