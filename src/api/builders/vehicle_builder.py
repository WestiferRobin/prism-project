from src.utils.configs.vehicle_config import VehicleConfig
from src.utils.enums import VehicleType
from src.app.models.app_models.equations.chemistry.mass import Mass
from src.app.models.app_models.vehicles import Vehicle
from zlegacy.app.models import Shuttle
from src.app.models.app_models.vehicles.speeder import Speeder


def build_vehicle(vehicle_type: VehicleType, mass: Mass) -> Vehicle:
    config = VehicleConfig(vehicle_type=vehicle_type, mass=mass)
    return Vehicle(config=config)


def build_speeder(config: VehicleConfig) -> Speeder:
    return Speeder(config=config)


def build_shuttle(config: VehicleConfig) -> Shuttle:
    return Shuttle(config=config)

