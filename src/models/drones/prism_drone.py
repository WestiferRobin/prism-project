from uuid import uuid4


class PrismCell:
    def __init__(self, seed):
        self.dna = seed

class PrismBrain:
    def __init__(self, seed):
        mass = []
        for i in range(0, 16):
            cells = []
            for j in range(0, 16):
                cells.append(PrismCell(seed))
            mass.append(cells)
        self.mass = mass

class PrismAgent:
    def __init__(self, seed = None):
        if seed is None:
            seed = uuid4()
        self.brain = PrismBrain(seed)

    def mass(self):
        return self.brain.mass

class PrismDrone(PrismAgent):
    def __init__(self, seed = None):
        super().__init__(seed)

if __name__ == "__main__":
    drone = PrismDrone()
    print(drone.mass())