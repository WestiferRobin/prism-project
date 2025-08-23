from uuid import UUID

from src.api.builders.config_builders.drone_configs import build_drone_config
from src.models.drones import Drone
from src.models.drones.legion_drone import LegionDrone
from src.utils.date import Date
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_drone(
    version: int,
    name: str = None,
    alias: str = None,
    dna: UUID = None,
    age: AgeType = None,
    gender: GenderType = None,
    race: RaceType = None,
    rank: RankType = None,
    date: Date = None
) -> Drone:
    drone_config = build_drone_config(
        version=version,
        name=name,
        alias=alias,
        dna=dna,
        age=age,
        gender=gender,
        race=race,
        rank=rank,
        date=date
    )
    return Drone(config=drone_config)


def build_legion_drone(
    version: int,
    name: str = None,
    alias: str = None,
    dna: UUID = None,
    age: AgeType = None,
    gender: GenderType = None,
    race: RaceType = None,
    rank: RankType = None,
    date: Date = None
) -> LegionDrone:
    drone_config = build_drone_config(
        version=version,
        name=name,
        alias=alias,
        dna=dna,
        age=age,
        gender=gender,
        race=race,
        rank=rank,
        date=date
    )
    return LegionDrone(config=drone_config)

