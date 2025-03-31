from src.models.prisms.model import PrismDrone


class LegionShip:
    def __init__(self, pilot: PrismDrone, engines: tuple, position: tuple = None):
        self.pilot = pilot
        self.engines = engines

        if position is None:
            position = (0, 0, 0, 0)
        self.position = position