import math

from src.models.equations.math.area import Area


def build_area(amount: float) -> Area:
    return Area(amount=amount)


def build_rectangle_area(length: float, width: float) -> Area:
    amount = length * width
    return build_area(amount=amount)


def build_square_area(length: float) -> Area:
    return build_rectangle_area(
        length=length,
        width=length,
    )


def build_circle_area(radius: float) -> Area:
    amount = math.pi * radius ** 2
    return build_area(amount=amount)

