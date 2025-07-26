from src.api.builders.config_builders.vehicle_configs import build_vehicle_config
from src.models.equations.mass import Mass
from src.models.vehicles import Vehicle
from src.models.vehicles.shuttle import Shuttle
from src.models.vehicles.speeder import Speeder
from src.utils.configs.model_configs.vehicle_config import VehicleConfig
from src.utils.enums.vehicle_enums import VehicleType


def build_vehicle(version: int, vehicle_type: VehicleType, mass: Mass) -> Vehicle:
    config = build_vehicle_config(
        version=version,
        mass=mass,
        vehicle_type=vehicle_type
    )
    return Vehicle(config=config)


def build_speeder(config: VehicleConfig) -> Speeder:
    return Speeder(config=config)


def build_shuttle(config: VehicleConfig) -> Shuttle:
    return Shuttle(config=config)

