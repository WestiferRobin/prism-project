from uuid import UUID

from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.configs.model_configs.vehicle_configs import VehicleConfig
from src.utils.enums.vehicle_enums import VehicleType


class SpeederConfig(VehicleConfig):
    def __init__(self, pilot_config: DroneConfig, **speeder_data):
        super().__init__(
            pilot_config=pilot_config,
            vehicle_type=VehicleType.Speeder,
            **speeder_data
        )

