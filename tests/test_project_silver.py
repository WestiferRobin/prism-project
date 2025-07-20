from src.api.builders.config_builder import build_speeder_config, build_shuttle_config
from src.api.builders.unit_builders.mass_builder import build_mass, build_kilo_mass
from src.api.builders.vehicle_builder import build_speeder, build_shuttle
from src.api.validators.vehicle_validator import validate_speeder, validate_shuttle
from tests.test_equations import test_math_equations, test_physics_equations


def test_equations():
    test_math_equations()
    test_physics_equations()


def test_speeder():
    mass = build_kilo_mass(1)
    speeder_config = build_speeder_config(mass)
    speeder = build_speeder(speeder_config)
    validate_speeder(speeder)


def test_shuttle():
    mass = build_kilo_mass(1)
    shuttle_config = build_shuttle_config(mass)
    shuttle = build_shuttle(shuttle_config)
    validate_shuttle(shuttle)

