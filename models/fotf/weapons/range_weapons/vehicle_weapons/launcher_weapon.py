from models.fotf.weapons.range_weapons.model import RangeWeapon


class Launcher(RangeWeapon):
    MAX_ROUNDS = 4
    def __init__(self, faces, rounds: int = 0):
        super().__init__(rounds, Launcher.MAX_ROUNDS, faces)

class MissileLauncher(Launcher):
    def __init__(self):
        super().__init__(rounds=Launcher.MAX_ROUNDS)

class BombLauncher(Launcher):
    def __init__(self):
        super().__init__(rounds=Launcher.MAX_ROUNDS-1)

