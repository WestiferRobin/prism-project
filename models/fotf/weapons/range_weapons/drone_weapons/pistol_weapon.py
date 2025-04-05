from models.fotf.weapons.range_weapons.drone_weapons.gun_weapon import Gun


class StandardPistol(Gun):
    MAX_ROUNDS = 3
    def __init__(self, rounds: int = None, faces: tuple = None):
        if rounds is None:
            rounds = StandardPistol.MAX_ROUNDS
        if faces is None:
            faces = (0, 0, 1, 1, 2, 3)
        super().__init__(rounds, StandardPistol.MAX_ROUNDS, faces)

class ShotPistol(StandardPistol):
    def __init__(self):
        super().__init__(faces=(0, 0, 0, 0, 4, 6))

class AutoPistol(StandardPistol):
    def __init__(self):
        super().__init__(faces=(0, 0, 1, 2, 2, 4))

class PrecisionPistol(StandardPistol):
    def __init__(self):
        super().__init__(faces=(0, 0, 1, 2, 2, 3))

class RevolverPistol(StandardPistol):
    def __init__(self):
        super().__init__(faces=(0, 0, 0, 2, 4, 6))

