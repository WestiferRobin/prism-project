from typing import List

from src.exceptions import EngineException
from src.materials import Metal, METALS


def metals_list() -> List[Metal]:
    return METALS.values()


def find_metal(metal_name: str) -> Metal:
    if metal_name.lower() not in METALS:
        raise EngineException("Unknown metal '{}'".format(metal_name))
    return METALS[metal_name.lower()]


def find_density(metal_name) -> float:
    return find_metal(metal_name).density

