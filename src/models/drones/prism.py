import random
import uuid

from src.utils.enums.prism_enums import LifeSpan, LegionRank
from src.utils.prism_utils import build_prism_cell, MAX_CELL_SIZE


class PrismCell:
    def __init__(self, seed):
        self.dna = seed
        self.cell = build_prism_cell(self.dna)

class Prism:
    def __init__(self, dna_id):
        self.age = 0
        self.id = dna_id

        nexus_mass = []
        for i in range(MAX_CELL_SIZE):
            cells = []
            for j in range(MAX_CELL_SIZE):
                prism_cell = PrismCell(self.id)
                cells.append(prism_cell)
            nexus_mass.append(cells)

        self.mass = nexus_mass

    def cells(self):
        return self.mass

class PrismDrone:
    drone_count = 0

    @staticmethod
    def get_valid_name():
        name = f"Drone #{PrismDrone.drone_count}"
        PrismDrone.drone_count += 1
        return name

    def __str__(self):
        return f"{self.rank.name} {self.__name}"

    def __init__(self,
                 prism_id = None,
                 name: str = None,
                 rank: LegionRank = LegionRank.Private,
                 sprite: str = None,
                 age: int = 20,
                 gender: bool = None
                 ):


        self.id = uuid.uuid4() if prism_id is None else prism_id
        self.brain = Prism(self.id)

        self.age = age
        self.rank = rank if self.age >= 20 else LegionRank.Student

        if name is None:
            name = PrismDrone.get_valid_name()
        self.__name = name
        self.name = self.__str__()

        if sprite is None:
            sprite = "O"
        self.sprite = sprite

        if gender is None: # Male is True 1, Female is False 0
            gender = random.choice([True, False])
        self.gender = gender
        self.network = {}

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

    def is_alive(self):
        pass

    def interact(self, target):
        # TODO: Need to figure this out soon...
        # if not self.in_range(target):
        #     return
        if target.id not in self.network:
            self.network[target.id] = 0

        source_cells = self.brain.cells()
        target_cells = target.brain.cells()
        if len(source_cells) != len(target_cells):
            raise Exception("PrismDrones can't interact due to brain cells")

        social_score = 0
        total_interactions = 0
        for i in range(0xF + 1):
            for j in range(0xF + 1):
                source_cell = source_cells[i][j].cell
                source_data = source_cell['data']
                data_keys = [ key for key in source_data.keys() ]

                target_cell = target_cells[i][j].cell
                target_data = target_cell['data']

                for source_key in data_keys:
                    source_band = source_data[source_key].hex
                    source_byte = int(source_band[0], 0xF + 1)

                    target_key = random.choice(data_keys)
                    target_band = target_data[target_key].hex
                    target_byte = int(target_band[0], 0xF + 1)

                    if source_byte + target_byte <= 0:
                        byte_score = target_byte + source_byte / 2
                    else:
                        byte_score = target_byte / (source_byte + target_byte)
                    if byte_score > 0.5:
                        social_score += 1
                    elif byte_score < 0.5:
                        social_score -= 1

                total_interactions += 1
        social_score = social_score / total_interactions

        self.network[target.id] += social_score

        return social_score


