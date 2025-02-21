from src.models.drones.prism import PrismDrone
from src.models.engines.nexus_engine import NexusEngine
from src.models.ships.model import LegionShip


class OrbDrone(LegionShip):
    def __init__(self, pilot: PrismDrone, engines: tuple = None, position: tuple = None):
        if engines is None:
            engines = tuple([NexusEngine(pilot.id)])

        if position is None:
            position = (0, 0, 0, 0)
        self.position = position

        super().__init__(pilot, engines, position)