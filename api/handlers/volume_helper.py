import math


def calculate_sphere_volume(radius: float) -> float:
    return (math.pi * radius ** 3) * (4 / 3)


def calculate_cube_volume(length: float, width: float, height: float) -> float:
    return length * width * height

