from typing import Tuple, List

from src.models.drones.model import Prism, PrismDrone
from src.models.vehicles.model import NexusEngine


class OrbDrone:
    def __init__(self, pilot: Prism, engines: Tuple = None):
        if engines is None:
            engines = (NexusEngine(pilot.id))
        self.pilot = pilot
        self.engines = engines


class SpaceSpeeder(OrbDrone):
    def __init__(self, pilot: PrismDrone):
        super().__init__(
            pilot=pilot.brain,
            engines=(
                NexusEngine(pilot.id),
                NexusEngine(pilot.id),
                NexusEngine(pilot.id),
                NexusEngine(pilot.id)
            )
        )
        self.position = (0, 0, 0)
        self.drone = pilot


class SpaceShuttle(OrbDrone):
    def __init__(self, pilot: PrismDrone, co_pilot: PrismDrone = None):
        super().__init__(
            pilot=pilot.brain,
            engines=(
                NexusEngine(pilot.id),
                NexusEngine(pilot.id),
                NexusEngine(pilot.id),
                NexusEngine(pilot.id)
            )
        )
        self.co_pilot = co_pilot


class RangeWeapon:
    def __init__(self, rounds: int):
        self.rounds = rounds
        self.current_rounds = self.rounds


class LaserCannon(RangeWeapon):
    def __init__(self, rounds=3):
        super().__init__(rounds)


class MissileLauncher(RangeWeapon):
    def __init__(self, rounds=2):
        super().__init__(rounds)


class SpaceFighter(SpaceSpeeder):
    def __init__(self, pilot: PrismDrone):
        super().__init__(pilot)
        self.right_cannon = LaserCannon()
        self.left_cannon = LaserCannon()

