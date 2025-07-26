from uuid import UUID

from src.utils.date import Date
from src.utils.configs import Config
from src.utils.enums.prism_enums import AgeType, GenderType, RankType, RaceType


class PrismConfig(Config):
    dna: UUID
    age: AgeType
    gender: GenderType
    race: RaceType
    rank: RankType
    birth_date: Date

    def __init__(self, **prism_data):
        super().__init__(**prism_data)

    @property
    def id(self) -> UUID:
        return self.dna

    @property
    def age_value(self) -> int:
        age_type = self.age_type
        return age_type.percent_value

