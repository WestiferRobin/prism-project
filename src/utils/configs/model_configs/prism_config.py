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

    @property
    def age(self) -> AgeType:
        # alias of
        return Date.convert_age(self.birth_date)


    

