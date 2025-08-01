from src.api.builders.config_builders.drone_configs import build_drone_config
from src.api.helpers.alias_helper import configure_alias
from src.api.helpers.name_helper import configure_name
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.enums.prism_enums import GenderType, RaceType, RankType, AgeType


def build_leader_config(
    version: int,
    rank: RankType,
    name: str = None,
    alias: str = None,
    leader_gender: GenderType = None,
    leader_race: RaceType = None
) -> DroneConfig:
    if leader_gender is None:
        leader_gender = GenderType.random_gender()
    if leader_race is None:
        leader_race = RaceType.random_race()
    if name is None:
        name = configure_name(
            gender=leader_gender,
            race=leader_race,
        )
    if alias is None:
        alias = configure_alias(name=name)
    return build_drone_config(
        version=version,
        name=name,
        alias=alias,
        age=AgeType.Adult,
        gender=leader_gender,
        race=leader_race,
        rank=rank
    )


