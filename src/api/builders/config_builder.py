from src.utils.configs import VehicleConfig
from src.utils.enums import VehicleType
from src.app.models.app_models.equations.chemistry.mass import Mass


def build_vehicle_config(
    vehicle_type: VehicleType,
    mass: Mass,
    name: str = None,
) -> VehicleConfig:
    return VehicleConfig(
        name=name,
        vehicle_type=vehicle_type,
        mass=mass
    )


def build_speeder_config(
    mass: Mass,
    name: str = None,
) -> VehicleConfig:
    return build_vehicle_config(
        vehicle_type=VehicleType.Speeder,
        mass=mass,
        name=name
    )


def build_shuttle_config(
    mass: Mass,
    name: str = None,
) -> VehicleConfig:
    return build_vehicle_config(
        vehicle_type=VehicleType.Shuttle,
        mass=mass,
        name=name
    )

