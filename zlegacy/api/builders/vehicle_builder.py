from src.utils.configs.vehicle_config import VehicleConfig
from src.utils.enums import VehicleType
from zlegacy.models.app_models import Mass
from zlegacy.models.app_models import Vehicle
from zlegacy.models import Shuttle
from zlegacy.models.app_models import Speeder


def build_vehicle(vehicle_type: VehicleType, mass: Mass) -> Vehicle:
    config = VehicleConfig(vehicle_type=vehicle_type, mass=mass)
    return Vehicle(config=config)


def build_speeder(config: VehicleConfig) -> Speeder:
    return Speeder(config=config)


def build_shuttle(config: VehicleConfig) -> Shuttle:
    return Shuttle(config=config)

