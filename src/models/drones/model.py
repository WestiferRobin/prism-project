import uuid

from src.utils.enums.prism_enums import LifeSpan, LegionRank
from src.utils.prism_utils import build_prism_nexus


class PrismCell:
    def __init__(self, seed):
        self.dna = seed


class Prism:
    def __init__(self, dna_id):
        self.mass = build_prism_nexus(dna_id)
        self.age = 0
        self.id = self.mass["id"]

    def dna_cells(self):
        cells_mass = self.mass["cells"]
        dna_cells = []
        for strand in cells_mass:
            cells = []
            for cell in strand:
                prism_cell = PrismCell(self.id)
                cells.append(prism_cell)
            dna_cells.append(cells)
        return dna_cells


class PrismDrone:
    drone_count = 0

    @staticmethod
    def get_valid_name():
        name = f"Drone #{PrismDrone.drone_count}"
        PrismDrone.drone_count += 1
        return name

    def __str__(self):
        return f"{self.rank} {self.name}"

    def __init__(self,
                 prism_id = None,
                 name: str = None,
                 rank: LegionRank = LegionRank.Private,
                 sprite: str = "O",
                 age: int = 20,
                 gender: bool = True
                 ):


        self.id = uuid.uuid4() if prism_id is None else prism_id
        self.brain = Prism(self.id)

        self.name = PrismDrone.get_valid_name() if name is None else name

        self.rank = rank if age >= 20 else LegionRank.Student
        self.sprite = sprite
        self.age = age
        self.gender = gender

        self.__apply_brain()

    def __apply_brain(self):
        cells = self.brain.dna_cells()

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


class PrismTrooper(PrismDrone):
    def __init__(self, dna_id):
        super().__init__(dna_id)


class PrismWorker(PrismDrone):
    def __init__(self, dna_id):
        super().__init__(dna_id)
