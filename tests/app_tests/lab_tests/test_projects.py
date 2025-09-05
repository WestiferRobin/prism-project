from src.api.builders.model_builders.lab_builders.density_builders import build_water_density
from src.api.builders.model_builders.lab_builders.mass_builder import build_cube_mass
from src.api.validators.model_validators.mass_validator import validate_mass


def test_ice_cube(volume_amount: int = 1, density_amount: int = 1):
    water_density = build_water_density(amount=density_amount)
    ice_cube = build_cube_mass(length=volume_amount, density=water_density)
    assert validate_mass(mass=ice_cube)


def test_metal_cube(volume_amount: int = 1, density_amount: int = 1):
    water_density = build_metal_density(amount=density_amount)
    metal_cube = build_cube_mass(length=volume_amount, density=water_density)
    assert validate_mass(mass=metal_cube)


def test_water_sphere(volume_amount: int = 1, density_amount: int = 1):
    water_density = build_water_density(amount=density_amount)
    water_sphere = build_cube_mass(length=volume_amount, density=water_density)
    assert validate_mass(mass=water_sphere)


def test_plasma_sphere(volume_amount: int = 1, density_amount: int = 1):
    density = build_water_density(amount=density_amount)
    plasma_sphere = build_cube_mass(length=volume_amount, density=density)
    assert validate_mass(mass=plasma_sphere)

