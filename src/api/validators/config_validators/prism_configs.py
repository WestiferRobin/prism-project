from uuid import UUID

from src.api.validators.config_validators import validate_config
from src.utils.configs.model_configs.prism_config import PrismConfig
from src.utils.date import Date
from src.utils.enums.prism_enums import AgeType, GenderType, RaceType, RankType


def validate_prism_config(config: PrismConfig):
    assert config.prism is not None
    assert isinstance(config.prism, PrismConfig)
    validate_config(config=config)

    assert config.dna is not None
    assert isinstance(config.dna, UUID)

    assert config.age is not None
    assert isinstance(config.age, AgeType)

    assert config.gender is not None
    assert isinstance(config.gender, GenderType)

    assert config.race is not None
    assert isinstance(config.race, RaceType)

    assert config.rank is not None
    assert isinstance(config.rank, RankType)

    assert config.birth_date is not None
    assert isinstance(config.birth_date, Date)


