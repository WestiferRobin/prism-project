import uuid

from src.utils.prism_utils import build_prism_nexus


class PrismAtom:
    def __init__(self, seed):
        self.particles = seed


class PrismCell:
    def __init__(self, seed):
        self.dna = seed


class Prism:
    def __init__(self, dna_id):
        self.mass = build_prism_nexus(dna_id)

    def cells(self):
        return self.mass["cells"]


class PrismAgent:
    def __init__(self, prism: Prism = None):
        self.brain = Prism(uuid.uuid4()) if prism is None else prism
        self.__apply_brain()

    def __apply_brain(self):
        mass = self.brain.mass()
        cells = mass["cells"]
        cells = self.brain.mass


class PrismDrone(PrismAgent):
    def __init__(self, dna_id):
        super().__init__(dna_id)

class PrismTrooper(PrismDrone):
    def __init__(self, dna_id):
        super().__init__(dna_id)





if __name__ == "__main__":
    brain = Prism(uuid.uuid4())
    print(brain.mass())
    agent = PrismAgent(brain)
    print(drone.brain())
    drone = PrismDrone
    print(drone.mass())
    # Then PrismAgents can go into OrbDrones
    # Then OrbDrones can go into NexusEngines
    # Then SpaceSpeeder can go into OrbDrone
