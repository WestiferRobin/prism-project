from src.models.drones.prism_drone import PrismDrone
from src.models.vehicles.model import Ship
from src.models.vehicles.parts.engines import NexusEngine


class SpaceShip(Ship):
    def __init__(self, pilot_id, copilot: PrismDrone):
        super().__init__(pilot_id, copilot, NexusEngine())

class SpaceSpeeder(SpaceShip):
    def __init__(self, pilot_id, copilot):
        super().__init__(pilot_id, copilot)

class SpaceFighter(SpaceShip):
    def __init__(self, pilot_id, copilot):
        super().__init__(pilot_id, copilot)

class SpaceShuttle(SpaceShip):
    def __init__(self, pilot_id, copilot):
        super().__init__(pilot_id, copilot)