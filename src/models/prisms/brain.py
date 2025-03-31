from src.models.prisms.cell import PrismCell
from src.utils.prism_utils import MAX_CELL_SIZE


class PrismBrain:
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