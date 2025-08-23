from src.api.builders.model_builders.lab_builders.volume_builder import build_cube_volume, build_sphere_volume
from src.models.equations.chemistry.density import Density
from src.models.equations.chemistry.mass import Mass, Volume


def build_mass(volume: Volume, density: Density) -> Mass:
    return Mass(
        volume=volume,
        density=density,
    )


def build_cube_mass(
    length: float,
    density: Density,
) -> Mass:
    return build_mass(
        volume=build_cube_volume(length=length),
        density=density
    )


def build_sphere_mass(
    radius: float,
    density: Density
) -> Mass:
    return build_mass(
        volume=build_sphere_volume(radius=radius),
        density=density
    )

