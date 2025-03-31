import random

from src.configs.prism_config import PrismConfig
from src.models.prisms.brain import PrismBrain


class PrismDrone:
    drone_count = 0

    def __str__(self):
        return self.config.title()

    def __init__(self, config: PrismConfig = None):
        if config is None:
            config = PrismConfig()
        self.config = config

        self.brain = PrismBrain(self.config.id)
        self.health = 100
        self.network = {}

        self.__apply_brain()

    def __apply_brain(self):
        cells = self.brain.cells()

    def is_alive(self):
        return self.health > 0

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
                data_keys = [key for key in source_data.keys()]

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
