from src.models.drones.model import PrismAgent, PrismDrone


class Engine:
    def __init__(self, ship_id):
        self.id = ship_id

class NexusEngine:
    def __init__(self, ship_id):
        super().__init__(ship_id)

class OrbDrone:
    def __init__(self, pilot: PrismAgent):
        self.engines = NexusEngine()
        self.pilot = pilot

class SpaceSpeeder(OrbDrone):
    def __init__(self, pilot: PrismDrone, co_pilot: PrismAgent):
        super().__init__(pilot.agent(), co_pilot)
        self.engines = (
            NexusEngine(),
            NexusEngine(),
            NexusEngine(),
            NexusEngine()
        )
        self.position = {

        }

class SpaceShuttle(Ship):
    def __init__(self, pilot: PrismDrone, co_pilot: PrismDrone, cargo: list = None):
        super(pilot.id, co_pilot.id)

class SpaceShip()
