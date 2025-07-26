from uuid import UUID

from src.api.validators.prism_validator import validate_prism
from src.app.drone import Drone
from src.utils.configs.model_configs.drone_config import DroneConfig


def validate_drone(drone: Drone) -> None:
    assert isinstance(drone, Drone)

    assert drone.id is not None
    assert isinstance(drone.id, UUID)

    assert drone.name is not None
    assert isinstance(drone.name, str)

    assert drone.config is not None
    assert isinstance(drone.config, DroneConfig)

    validate_prism(drone.prism)

    assert drone.prism.dna == drone.id


