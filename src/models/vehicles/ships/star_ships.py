from src.models.drones.prism_drone import PrismDrone
from src.models.vehicles.model import Ship
from src.models.vehicles.parts.engines import NexusEngine


class StarShip(Ship):
    def __init__(self, captain_id, copilot: PrismDrone):
        super().__init__(captain_id, copilot, NexusEngine())

class SolarDreadnought(StarShip): # Citadel
    def __init__(self, captain_id, copilot):
        super().__init__(captain_id, copilot)

class CapitalShip(StarShip): # City, Town
    def __init__(self, captain_id, copilot):
        super().__init__(captain_id, copilot)

class FrigateShip(StarShip): # Town, Outposts
    def __init__(self, captain_id, copilot):
        super().__init__(captain_id, copilot)

class CruiserShip(StarShip): # Outposts, Camps
    def __init__(self, captain_id, copilot):
        super().__init__(captain_id, copilot)