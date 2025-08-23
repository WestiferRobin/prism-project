from src.api.builders.model_builders.lab_builders.area_builders import build_rectangle_area, build_circle_area
from src.models.equations.chemistry.mass import Volume
from src.models.equations.math.area import Area


def build_volume(area: Area, length: float) -> Volume:
    return Volume(area=area, length=length)


def build_rectangle_volume(length: float, width: float, height: float) -> Volume:
    base_area = build_rectangle_area(length=length, width=width)
    return build_volume(area=base_area, length=height)


def build_cube_volume(length: float) -> Volume:
    return build_rectangle_volume(length=length, width=length, height=length)


def build_sphere_volume(radius: float) -> Volume:
    circle_area = build_circle_area(radius=radius)
    return build_volume(area=circle_area, length=radius)

