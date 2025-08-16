from src.models.equations.mass import Mass, Volume
from src.utils.enums.prefix_enums import PrefixType
from src.utils.enums.unit_enums import UnitType


def build_mass(mass_volume: Volume, mass_density: Density) -> Mass:
    return Mass(volume)


def build_mass_amount(
    volume_amount: float,
    mass_density: Density,

) -> Mass:
    mass_volume = build_volume(amount=volume_amount)
    return build_mass(
        mass_volume=
    )


def build_cube_mass(
    length: float,
    length_type: UnitType.METER,
    length_prefix: PrefixType = PrefixType.NONE
) -> Mass:



def build_sphere_mass(
    radius: float,
    radius_type: UnitType.METER,
    radius_prefix: PrefixType = PrefixType.NONE
) -> Mass:
    pass