from src.api.builders.config_builder import build_speeder_config
from src.api.builders.unit_builders.mass_builder import build_kilo_mass
from src.api.builders.vehicle_builder import build_speeder
from src.api.validators.vehicle_validator import validate_speeder


def run_engine():
    mass = build_kilo_mass(1)
    speeder_config = build_speeder_config(mass)
    speeder = build_speeder(speeder_config)
    validate_speeder(speeder)

