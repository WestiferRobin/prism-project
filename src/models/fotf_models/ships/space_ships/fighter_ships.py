from src.models.prisms.model import PrismDrone
from src.models.fotf_models.ships.space_ships.speeder_ships import SpaceSpeeder
from src.models.fotf_models.weapons.range_weapons.vehicle_weapons.launcher_weapon import MissileLauncher, BombLauncher, Launcher
from src.models.fotf_models.weapons.range_weapons.vehicle_weapons.cannon_weapon import LaserCannon, PlasmaCannon, IonCannon


class SpaceFighter(SpaceSpeeder):
    def __init__(self,
                 pilot: PrismDrone,
                 right_cannon: LaserCannon = None,
                 left_cannon: LaserCannon = None,
                 launcher: Launcher = None
     ):
        super().__init__(pilot, right_cannon, left_cannon)
        self.armor = 50
        self.shields = 25

        if launcher is None:
            launcher = MissileLauncher()
        self.launcher = launcher

class SpaceInterceptor(SpaceFighter):
    def __init__(self, pilot: PrismDrone):
        super().__init__(pilot, PlasmaCannon(), PlasmaCannon(), MissileLauncher())
        self.shields += 25

class SpaceBomber(SpaceFighter):
    def __init__(self, pilot: PrismDrone, co_pilot: PrismDrone):
        super().__init__(pilot, IonCannon(), IonCannon(), BombLauncher())
        self.co_pilot = co_pilot
        self.shields += 25
        self.armor += 25