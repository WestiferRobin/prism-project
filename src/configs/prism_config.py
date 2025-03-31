import random
import uuid

from src.utils.enums.prism_enums import LegionRank, LifeSpan

DRONE_COUNT = 0


def get_valid_name():
    global DRONE_COUNT
    DRONE_COUNT += 1
    name = f"Drone #{DRONE_COUNT}"
    return name


class PrismConfig:
    def __init__(self,
                 prism_id=None,
                 name: str = None,
                 age: int = 20,
                 rank: LegionRank = LegionRank.Private,
                 gender: bool = None,
                 sprite: str = None):

        self.id = uuid.uuid4() if prism_id is None else prism_id

        if name is None:
            name = get_valid_name()

        self.name = name

        self.age = age

        self.rank = rank if self.age >= 20 else LegionRank.Student

        if gender is None:  # Male is True 1, Female is False 0
            gender = random.choice([True, False])
        self.gender = gender

        if sprite is None:
            sprite = "O"
        self.sprite = sprite

    def title(self):
        return f"{self.rank} {self.name}"

    def life_span(self):
        if self.age <= 0:
            return LifeSpan.Baby
        elif 1 <= self.age <= 5:
            return LifeSpan.Toddler
        elif 6 <= self.age <= 12:
            return LifeSpan.Child
        elif 13 <= self.age <= 19:
            return LifeSpan.Teen
        elif 20 <= self.age <= 79:
            return LifeSpan.Adult
        else:
            return LifeSpan.Elder

