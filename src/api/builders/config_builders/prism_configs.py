from uuid import UUID, uuid4

from src.api.helpers.alias_helper import configure_alias
from src.api.helpers.name_helper import configure_name
from src.utils.constants.date_constants import CURRENT_YEAR
from src.utils.date import Date
from src.utils.configs.model_configs.prism_config import PrismConfig
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_prism_config(
    version: int,
    name: str = None,
    alias: str = None,
    dna: UUID = None,
    age: AgeType = AgeType.Adult,
    gender: GenderType = None,
    race: RaceType = None,
    rank: RankType = None,
    date: Date = None,
) -> PrismConfig:
    if dna is None:
        dna = uuid4()
    if gender is None:
        gender = GenderType.random_gender()
    if race is None:
        race = RaceType.random_race()
    if rank is None:
        rank = RankType.random_rank()
    if name is None:
        name = configure_name(gender=gender, race=race)
    if alias is None:
        alias = configure_alias(name=name)

    if date is None:
        date = Date.random_date()
        date.year = CURRENT_YEAR - age.value

    return PrismConfig(
        version=version,
        config_id=dna,
        name=name,
        alias=alias,

        gender=gender,
        race=race,
        rank=rank,
        birth_date=date
    )

