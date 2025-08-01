from src.api.builders.config_builders.drone_configs import build_drone_config
from src.utils.configs.model_configs.drone_config import DroneConfig
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def build_ozzy_config(version: int) -> DroneConfig:
    ozzy_config = build_drone_config(
        version=version,
        name="Ozzy Osborne",
        alias="wes-omega",
        age=AgeType.Adult,
        gender=GenderType.Male,
        race=RaceType.Human,
        rank=RankType.Arch,
    )
    return ozzy_config


def build_gordon_config(version: int) -> DroneConfig:
    gordon_config = build_drone_config(
        version=version,
        name="Gordon Ramsey",
        alias="gordon-ramsey",
        age=AgeType.Adult,
        gender=GenderType.Male,
        race=RaceType.Human,
        rank=RankType.Arch
    )
    return gordon_config


def build_harrison_config(version: int) -> DroneConfig:
    gordon_config = build_drone_config(
        version=version,
        name="Harrison Ford",
        alias="harrison-ford",
        age=AgeType.Adult,
        gender=GenderType.Male,
        race=RaceType.Human,
        rank=RankType.Arch
    )
    return gordon_config


def build_patrick_config(version: int) -> DroneConfig:
    patrick_config = build_drone_config(
        version=version,
        name="Patrick Stewart",
        alias="patrick-stewart",
        age=AgeType.Adult,
        gender=GenderType.Male,
        race=RaceType.Human,
        rank=RankType.Arch
    )
    return patrick_config



def build_clint_config(version: int) -> DroneConfig:
    clint_config = build_drone_config(
        version=version,
        name="Clint Eastwood",
        alias="clint-eastwood",
        age=AgeType.Adult,
        gender=GenderType.Male,
        race=RaceType.Human,
        rank=RankType.Arch
    )
    return clint_config

