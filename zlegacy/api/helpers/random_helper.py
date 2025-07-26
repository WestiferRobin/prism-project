import random
from typing import Any

from zlegacy.api.builders.unit_builders.mass_builder import build_mass
from src.utils.enums import VehicleType, UnitType, PrefixType
from zlegacy.models.app_models import Mass


def random_item(item_list: list) -> Any:
    return random.choice(item_list)


def random_unit_type() -> UnitType:
    unit_types = list(value for value in UnitType)
    return random_item(unit_types)


def random_prefix_type() -> PrefixType:
    prefix_types = list(value for value in PrefixType)
    return random_item(prefix_types)


def random_vehicle_type() -> VehicleType:
    vehicle_types = list(value for value in VehicleType)
    return random_item(vehicle_types)


def random_vehicle_mass() -> Mass:
    amount = random.random() * float("inf")
    prefix = random_prefix_type()
    mass = build_mass(amount=amount, prefix=prefix)
    return mass

def

def random_droid_name() -> str: