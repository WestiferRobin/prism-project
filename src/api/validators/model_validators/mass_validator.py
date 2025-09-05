from src.api.builders.model_builders.lab_builders.density_builders import build_density
from src.api.builders.model_builders.lab_builders.mass_builder import build_mass
from src.api.builders.model_builders.lab_builders.volume_builder import build_volume
from src.models.equations.chemistry.density import Density
from src.models.equations.chemistry.mass import Mass
from src.models.equations.math.volume import Volume
from src.utils.unit import Unit


def validate_unit(unit: Unit, expected_unit: Unit):
    assert unit is not None
    assert type(unit) is Unit

    assert unit.type == expected_unit.type
    assert unit.prefix == expected_unit.prefix
    assert unit.amount == expected_unit.amount
    assert unit.value == expected_unit.value
    assert f"{unit}" == f"{expected_unit}"

    return True


def validate_volume(volume: Volume, expected_volume: Volume) -> bool:
    assert validate_unit(unit=volume.volume, expected_unit=expected_volume.volume)
    return True


def validate_density(density: Density, expected_density: Density) -> bool:
    assert validate_unit(unit=density, expected_unit=expected_density)
    return True


def validate_mass(mass: Mass) -> bool:
    assert mass is not None
    assert type(mass) is Mass
    assert validate_unit(
        unit=mass,
        expected_unit=build_mass(
            volume=mass.volume,
            density=mass.density
        )
    )

    assert mass.volume is not None
    mass_volume = mass.volume
    expected_volume = build_volume(area=mass_volume.area, length=mass_volume.length)
    assert validate_volume(volume=mass.volume, expected_volume=expected_volume)

    assert mass.density is not None
    mass_density = mass.density
    expected_density = build_density(amount=mass_density.amount, prefix=mass_density.prefix)
    assert validate_density(density=mass_density, expected_density=expected_density)

    return True

