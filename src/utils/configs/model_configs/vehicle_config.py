from src.models.equations.mass import Mass
from src.utils.configs import Config
from src.utils.enums.vehicle_enums import VehicleType


class VehicleConfig(Config):
    type: VehicleType
    mass: Mass

    def __init__(self,
        vehicle_type: VehicleType,
        mass: Mass,
        name: str = None,
        **vehicle_data
    ):
        if name is None:
            name = vehicle_type.name
        super().__init__(
            name=name,
            type=vehicle_type,
            mass=mass,
            **vehicle_data
        )

