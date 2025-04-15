import torch
from torch import nn

from configs.prism_config import MAX_CELL_SIZE
from models.prisms.prism_parts.cell import PrismCell


class PrismBrain(nn.Module):
    def __init__(self, dna_id):
        super(PrismBrain, self).__init__()
        self.age = 0
        self.id = dna_id

        self.mass = nn.ModuleList([
            nn.ModuleList([PrismCell(self.id) for _ in range(MAX_CELL_SIZE)])
            for _ in range(MAX_CELL_SIZE)
        ])

    def cells(self):
        return self.mass

    def forward(self, input_tensor):
        outputs = []
        chunk_size = 8  # Each cell receives 8 inputs
        flat_inputs = input_tensor.view(-1, chunk_size)

        for i, row in enumerate(self.mass):
            for j, cell in enumerate(row):
                idx = i * MAX_CELL_SIZE + j
                if idx < flat_inputs.shape[0]:
                    outputs.append(cell(flat_inputs[idx]))
        return torch.cat(outputs, dim=0)

    def learn(self, feedback: float):
        for row in self.mass:
            for cell in row:
                cell.learn(feedback)
