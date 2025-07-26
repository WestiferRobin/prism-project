from src.models.equations.mass import Mass
from src.utils.configs.model_configs.vehicle_config import VehicleConfig
from src.utils.enums.vehicle_enums import VehicleType


def build_vehicle_config(
        version: int,
        mass: Mass,
        vehicle_type: VehicleType,
        name: str = None,
        alias: str = None
) -> VehicleConfig:
    return VehicleConfig(
        version=version,
        name=name,
        alias=alias,
        vehicle_type=vehicle_type,
        mass=mass
    )

