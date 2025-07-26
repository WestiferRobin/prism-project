from uuid import UUID, uuid4

from src.api.helpers.alias_helper import create_alias
from src.models.date import Date
from src.utils.configs.prism_config import PrismConfig
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_prism_config(
    version: int,
    name: str,
    alias: str = None,
    dna: UUID = None,
    age: AgeType = None,
    gender: GenderType = None,
    race: RaceType = None,
    rank: RankType = None,
    date: Date = None,
) -> PrismConfig:
    if alias is None:
        alias = create_alias(name=name)
    if dna is None:
        dna = uuid4()
    if age is None:
        age = AgeType.random_age()
    if gender is None:
        gender = GenderType.random_gender()
    if race is None:
        race = RaceType.random_race()
    if rank is None:
        rank = RankType.random_rank()
    return PrismConfig(
        version=version,
        name=name,
        alias=alias,
        dna=dna,
        age=age,
        gender=gender,
        race=race,
        rank=rank,
        birth_date=date
    )

