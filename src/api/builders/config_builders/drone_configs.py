from uuid import UUID

from src.api.builders.config_builders.prism_configs import build_prism_config
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.date import Date
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_drone_config(
    version: int,
    name: str = None,
    alias: str = None,
    dna: UUID = None,
    age: AgeType = None,
    gender: GenderType = None,
    race: RaceType = None,
    rank: RankType = None,
    date: Date = None
) -> DroneConfig:
    prism_config = build_prism_config(
        version=version,
        name=name,
        alias=alias,
        dna=dna,
        age=age,
        gender=gender,
        race=race,
        rank=rank,
        date=date,
    )
    return DroneConfig(prism_config=prism_config)

