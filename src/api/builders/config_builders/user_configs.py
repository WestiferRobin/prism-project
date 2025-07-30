from uuid import UUID, uuid4

from src.utils.configs.model_configs.user_config import UserConfig
from src.utils.constants import AVATAR_ID
from src.utils.date import Date
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_user_config(
        version: int,
        name: str,
        age: AgeType,
        gender: GenderType,
        birth_date: Date,
        user_id: UUID = None
) -> UserConfig:
    if user_id is None:
        user_id = uuid4()
    return UserConfig(
        version=version,
        name=name,
        user_id=user_id,
        age=age,
        gender=gender,
        race=RaceType.Human,
        rank=RankType.Private,
        birth_date=birth_date
    )


def build_wes_config(version: int) -> UserConfig:
    wes_id = AVATAR_ID
    return build_user_config(
        version=version,
        name="Wes Webb",
        alias="wes-black",
        age=AgeType.find_type(age=32),
        gender=GenderType.Male,
        birth_date=Date(year=1993, month=3, day=12),
        user_id=wes_id,
    )


def build_emma_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        name="Emma Burley",
        age=AgeType.find_type(30),
        gender=GenderType.Female,
        birth_date=Date(year=1994, month=8, day=24)
    )


def build_mary_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        name="Mary",
        age=AgeType.find_type(56),
        gender=GenderType.Female,
        birth_date=Date(year=1969, month=8, day=18)
    )


def build_max_config(version: int) -> UserConfig:
    return build_user_config(
        version=version,
        name="Max",
        age=AgeType.find_type(32),
        gender=GenderType.Male,
        birth_date=Date(year=1993, month=2, day=19)
    )

