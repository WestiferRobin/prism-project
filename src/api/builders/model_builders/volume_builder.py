from src.models.equations.mass import Volume
from src.models.equations.math.area import Area


def build_volume(area: Area, length: float) -> Volume:
    return Volume(area=area, length=length)


def build_rectangle_volume(length: float, width: float, height: float) -> Volume:
    area = build_rectangle_area
    return build_volume()


def build_cube_volume(length: float) -> Volume:
    return build_rectangle_volume(length=length, width=length, height=length)


def build_sphere_volume(radius: float) -> Volume:
    return build_volume()

