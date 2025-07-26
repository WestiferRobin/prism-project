from src.utils.enums import VehicleType
from src.utils.configs import Config
from zlegacy.models.app_models import Mass


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

