import torch
from torch import nn


class PrismCell(nn.Module):
    def __init__(self, seed):
        super(PrismCell, self).__init__()
        torch.manual_seed(abs(hash(seed)) % (2**32))
        self.net = nn.Sequential(
            nn.Linear(8, 16),
            nn.Tanh(),
            nn.Linear(16, 1),
            nn.Tanh()
        )
        for layer in self.net:
            if isinstance(layer, nn.Linear):
                nn.init.kaiming_uniform_(layer.weight, nonlinearity='relu')
        self.memory = torch.rand(8)

    def forward(self, input_vector):
        return self.net(input_vector)

    def learn(self, feedback):
        self.memory = self.memory + feedback * torch.randn_like(self.memory) * 0.01
        self.memory = torch.clamp(self.memory, 0.0, 1.0)
