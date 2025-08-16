from uuid import UUID

from src.utils.configs.model_configs.prism_config import PrismConfig
from src.utils.date import Date
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def validate_prism_config(source_config: PrismConfig, target_config: PrismConfig):
    assert source_config is not None
    assert isinstance(source_config, PrismConfig)

    assert source_config.version == target_config.version
    assert type(source_config.id) is UUID
    assert type(source_config.name) is str
    assert type(source_config.alias) is str

    assert source_config.dna is not None
    assert type(source_config.dna) is UUID
    assert source_config.dna == source_config.id

    assert source_config.age is not None
    assert isinstance(source_config.age, AgeType)
    assert source_config.age == target_config.age

    assert source_config.gender is not None
    assert type(source_config.gender) is GenderType

    assert source_config.race is not None
    assert type(source_config.race) is RaceType

    assert source_config.rank is not None
    assert type(source_config.rank) is RankType

    assert source_config.birth_date is not None
    assert type(source_config.birth_date) is Date

