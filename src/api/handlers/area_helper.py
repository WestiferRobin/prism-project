import math


def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2


def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height


def calculate_square_area(length: float) -> float:
    return calculate_rectangle_area(length, length)


def calculate_triangle_area(width: float, height: float) -> float:
    return (width * height) / 2

