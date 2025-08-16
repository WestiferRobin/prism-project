from utils.validators.config_validators.legion_configs import validate_legion_config
from utils.validators.model_validators.drone_validator import validate_legion_drone
from src.models.drones.legion_drone import LegionDrone
from src.models.legion import Legion
from src.utils.configs.model_configs.legion_config import LegionConfig


def validate_legion(legion: Legion):
    assert legion is not None
    assert isinstance(legion, Legion)

    assert legion.config is not None
    assert isinstance(legion.config, LegionConfig)
    validate_legion_config(source_config=legion.config)

    assert legion.admin is not None
    assert isinstance(legion.admin, LegionDrone)
    validate_legion_drone(drone=legion.admin)

    assert legion.vice is not None
    assert isinstance(legion.vice, LegionDrone)
    validate_legion_drone(drone=legion.vice)

    assert legion.general is not None
    assert isinstance(legion.general, LegionDrone)
    validate_legion_drone(drone=legion.general)

    assert legion.admiral is not None
    assert isinstance(legion.admiral, LegionDrone)
    validate_legion_drone(drone=legion.admiral)

