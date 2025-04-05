from utils.nexus_utils.prism_utils import build_prism_cell


class PrismCell:
    def __init__(self, seed):
        self.dna = seed
        self.cell = build_prism_cell(self.dna)
