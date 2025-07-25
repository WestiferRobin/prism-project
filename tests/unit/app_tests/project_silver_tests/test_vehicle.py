from zlegacy.api.builders import build_vehicle
from zlegacy.api.helpers import random_vehicle_type, random_vehicle_mass
from zlegacy.api.validators import validate_vehicle


def test_vehicle():
    vehicle_type = random_vehicle_type()
    vehicle_mass = random_vehicle_mass()
    vehicle = build_vehicle(
        vehicle_type=vehicle_type,
        mass=vehicle_mass,
    )
    validate_vehicle(vehicle)

