from uuid import UUID

from src.utils.configs import Config
from src.utils.enums.prism_enums import AgeType, GenderType, RankType


class PrismConfig(Config):
    dna: UUID
    name: str
    age: AgeType
    gender: GenderType
    rank: RankType


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def id(self) -> UUID:
        return self.dna

    @property
    def age_value(self) -> int:
        age_type = self.age_type
        return age_type.percent_value

