from zlegacy.api.builders import build_speeder_config, build_shuttle_config
from zlegacy.api.builders import build_kilo_mass
from src.api.builders.model_builders.vehicle_builder import build_speeder, build_shuttle
from zlegacy.api.validators import validate_speeder, validate_shuttle


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

