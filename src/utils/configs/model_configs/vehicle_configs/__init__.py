from uuid import UUID

from src.utils.configs import Config
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.enums.vehicle_enums import VehicleType


class VehicleConfig(Config):
    pilot_config: DroneConfig
    type: VehicleType
    # mass: Mass TODO: Apply this when we're doing labs

    def __init__(self,
        pilot_config: DroneConfig,
        vehicle_type: VehicleType,
        **vehicle_data
    ):
        super().__init__(
            config_id=pilot_config.id,
            pilot_config=pilot_config,
            type=vehicle_type,
            **vehicle_data
        )

