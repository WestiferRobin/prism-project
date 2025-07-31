from uuid import UUID, uuid4

from src.api.converters.date_converter import convert_to_date
from src.api.helpers.id_helper import create_user_id
from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.date import Date
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_user_config(
    version: int,
    user_id: UUID,
    name: str,
    alias: str,

    gender: GenderType,
    birth_date: Date,

    rank: RankType = RankType.Arch,
    race: RaceType = RaceType.Human,
) -> UserConfig:
    return UserConfig(
        version=version,
        user_id=user_id,
        name=name,
        alias=alias,

        gender=gender,
        race=race,
        rank=rank,
        birth_date=birth_date
    )


def build_wes_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        user_id=create_user_id('0'),
        name="Wes Black",
        alias="wes-omega",

        gender=GenderType.Male,
        birth_date=convert_to_date(month=3, day=12, year=1993)
    )


def build_emma_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        user_id=create_user_id('A'),
        name="Emma Green",
        alias="emma-gamma",

        gender=GenderType.Female,
        birth_date=convert_to_date(month=8, day=24, year=1994)
    )


def build_mary_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        user_id=create_user_id('B'),
        name="Mary Gold",
        alias="mary-lambda",

        gender=GenderType.Female,
        birth_date=convert_to_date(month=8, day=18, year=1969)
    )


def build_max_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        user_id=create_user_id('C'),
        name="Max Alpha",
        alias="max-alpha",

        gender=GenderType.Female,
        birth_date=convert_to_date(month=2, day=19, year=1993)
    )


def build_tyler_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        user_id=create_user_id('D'),
        name="Tyler Cyan",
        alias="tyler-theta",

        gender=GenderType.Male,
        birth_date=convert_to_date(month=3, day=6, year=1996)
    )


def build_payton_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        user_id=create_user_id('E'),
        name="Payton White",
        alias="payton-mu",

        gender=GenderType.Male,
        birth_date=convert_to_date(month=5, day=16, year=2000)
    )


def build_brian_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        user_id=create_user_id('F'),
        name="Brian Grey",
        alias="brian-tau",

        gender=GenderType.Male,
        birth_date=convert_to_date(month=11, day=28, year=1979)
    )












