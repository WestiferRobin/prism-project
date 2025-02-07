import uuid

from src.utils.enums.prism_enums import LifeSpan, DroneRank
from src.utils.prism_utils import build_prism_nexus


class PrismCell:
    def __init__(self, seed):
        self.dna = seed


class Prism:
    def __init__(self, dna_id):
        self.mass = build_prism_nexus(dna_id)
        self.age = 0
        self.id = self.mass["id"]

    def cells(self):
        return self.mass["cells"]


class PrismDrone:
    def __init__(self,
                 prism: Prism = None,
                 rank: DroneRank = DroneRank.Private,
                 sprite: str = "O",
                 age: int = 20
                 ):
        self.id = uuid.uuid4() if prism is None else prism.id
        self.brain = Prism(self.id) if prism is None else prism
        self.xp = rank if age >= 20 else DroneRank.Student
        self.sprite = sprite
        self.age = age

        self.__apply_brain()

    def __apply_brain(self):
        cells = self.brain.cells()

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


class PrismAvatar(PrismDrone):
    def __init__(self, avatar_sprite: str, user_id=None):
        if user_id is None:
            user_id = uuid.uuid4()
        super().__init__(sprite=avatar_sprite, prism=Prism(dna_id=user_id))


class PrismTrooper(PrismDrone):
    def __init__(self, dna_id):
        super().__init__(dna_id)


class PrismWorker(PrismDrone):
    def __init__(self, dna_id):
        super().__init__(dna_id)
