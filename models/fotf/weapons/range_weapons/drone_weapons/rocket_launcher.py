from models.fotf.weapons.range_weapons.model import RangeWeapon
from models.fotf.weapons.range_weapons.vehicle_weapons.launcher_weapon import Launcher

class GrenadeLauncher(RangeWeapon):
    def __init__(self):
        super().__init__(rounds=Launcher.MAX_ROUNDS-2)

class RocketLauncher(RangeWeapon):
    def __init__(self):
        super().__init__(rounds=Launcher.MAX_ROUNDS-3)
        