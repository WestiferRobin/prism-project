import random

from configs.prism_config import PrismConfig, MAX_CELL_SIZE
from models.prisms.prism_parts.brain import PrismBrain
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


class PrismDrone:

    def __init__(self, config: PrismConfig = None):
        if config is None:
            config = PrismConfig("PrismDrone")
        self.config = config

        self.brain = PrismBrain(self.config.id)
        self.health = 100
        self.network = {}

        self.__apply_brain()

    def __str__(self):
        return self.config.name

    def __apply_brain(self):
        dummy_input = torch.zeros(MAX_CELL_SIZE * MAX_CELL_SIZE * 8)
        self.state_tensor = self.brain.forward(dummy_input)

    def is_alive(self):
        return self.health > 0

    def interact(self, target):
        dummy_input = torch.zeros(MAX_CELL_SIZE * MAX_CELL_SIZE * 8)
        target_state = target.brain.forward(dummy_input)
        self_output = self.brain.forward(dummy_input)
        score = F.cosine_similarity(self_output, target_state, dim=0).item()
        return score

    def train_on_data(self, input_tensor, target_tensor, epochs=10):
        optimizer = optim.Adam(self.brain.parameters(), lr=0.003)
        loss_fn = nn.MSELoss()
        for epoch in range(epochs):
            optimizer.zero_grad()
            output = self.brain(input_tensor)
            loss = loss_fn(output, target_tensor)
            loss.backward()
            optimizer.step()
            if epoch % 10 == 0 or epoch == epochs - 1:
                print(f"Epoch {epoch}: Loss = {loss.item():.6f}")


class PrismFamily:
    def __init__(self, father: PrismDrone, mother: PrismDrone, children: list = None):
        self.father = father
        self.mother = mother
        self.members = {
            "father": self.father,
            "mother": self.mother,
            "children": {child.config.id: child for child in children}
        }

    def breed(self, random_chance: bool = False):
        if random_chance:
            if random.choice([True, False]):
                return None
        # TODO: Figure out the dna sequencing when two prisms breed
        child = PrismDrone()
        self.members["children"][child.config.id] = child
        return child
