from src.api.builders.model_builders.volume_builder import build_cube_volume, build_sphere_volume
from src.models.equations.mass import Mass
from utils.validators.model_validators.mass_validator import verify_mass


def test_mass(mass: Mass = None):
    if mass is None:
        mass = Mass()
    assert verify_mass(mass=mass)


def test_ice_cube():
    cube = build_cube_volume(length=1)
    water_density = build_water_density()
    ice_temperature = convert_celsius_to_kelvin(0)
    ice_cube = build_mass(
        volume=cube,
        density=water_density,
        temperature=ice_temperature
    )
    test_mass(mass=ice_cube)


def test_water_sphere():
    sphere = build_sphere_volume(radius=1)
    water_density = build_water_density()
    room_temperature = convert_celsius_to_kelvin(50)
    water_sphere = build_mass(
        volume=sphere,
        density=water_density,
        temperature=room_temperature
    )
    test_mass(mass=water_sphere)


def test_vapor_cube():
    cube = build_cube_volume(length=1)
    water_density = build_water_density()
    vapor_temperature = convert_celsius_to_kelvin(100)
    vapor_cube = build_mass(
        volume=cube,
        density=water_density,
        temperature=vapor_temperature
    )
    test_mass(mass=vapor_cube)


def test_plasma_sphere():
    sphere = build_sphere_volume(radius=1)
    water_density = build_water_density()
    plasma_temperature = convert_celsius_to_kelvin(20000)
    plasma_sphere = build_mass(
        volume=sphere,
        density=water_density,
        temperature=plasma_temperature
    )
    test_mass(mass=plasma_sphere)

