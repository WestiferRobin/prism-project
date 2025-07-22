from api.builders.vehicle_builder import build_vehicle
from api.helpers.random_helper import random_vehicle_type, random_vehicle_mass
from api.validators.vehicle_validator import validate_vehicle


def test_vehicle():
    vehicle_type = random_vehicle_type()
    vehicle_mass = random_vehicle_mass()
    vehicle = build_vehicle(
        vehicle_type=vehicle_type,
        mass=vehicle_mass,
    )
    validate_vehicle(vehicle)

