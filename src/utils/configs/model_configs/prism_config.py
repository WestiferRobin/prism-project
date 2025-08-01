from uuid import UUID

from src.utils.date import Date
from src.utils.configs import Config
from src.utils.enums.prism_enums import AgeType, GenderType, RankType, RaceType


class PrismConfig(Config):
    gender: GenderType
    race: RaceType
    rank: RankType
    birth_date: Date

    def __init__(self, **prism_data):
        super().__init__(**prism_data)

    @property
    def dna(self) -> UUID:
        return self.id

    def age(self, current_date: Date) -> AgeType:
        year_difference = current_date.year - self.birth_date.year
        return AgeType.find_type(age=year_difference)


    

