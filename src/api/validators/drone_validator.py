from uuid import UUID

from src.api.validators.prism_validator import validate_prism
from src.models.drones import Drone
from src.models.drones.legion_drone import LegionDrone
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


def validate_legion_drone(drone: LegionDrone) -> None:
    assert drone is not None
    assert isinstance(drone, LegionDrone)
    validate_drone(drone=drone)

    assert drone.health is not None
    assert isinstance(drone.health, int)

    assert drone.armor is not None
    assert isinstance(drone.armor, int)

    assert drone.shields is not None
    assert isinstance(drone.shields, int)

