from utils.enums import VehicleType
from app.configs import Config
from app.models.equations.chemistry.mass import Mass


class VehicleConfig(Config):
    type: VehicleType
    mass: Mass

    def __init__(self, vehicle_type: VehicleType, mass: Mass, name: str = None):
        if name is None:
            name = vehicle_type.name
        super().__init__(
            name=name,
            type=vehicle_type,
            mass=mass
        )

