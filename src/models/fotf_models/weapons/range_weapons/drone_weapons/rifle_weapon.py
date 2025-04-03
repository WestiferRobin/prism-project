from src.models.fotf_models.weapons.range_weapons.drone_weapons.gun_weapon import Gun

class StandardRifle(Gun):
    MAX_ROUNDS = 6
    def __init__(self, rounds: int, faces: tuple = None):
        if faces is None:
            faces = (0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3)
        super().__init__(rounds, StandardRifle.MAX_ROUNDS, faces)

class BattleRifle(StandardRifle):
    def __init__(self):
        super().__init__(StandardRifle.MAX_ROUNDS, faces=(0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5))

class AssaultRifle(StandardRifle):
    def __init__(self):
        super().__init__(StandardRifle.MAX_ROUNDS, faces=(0, 0, 0, 1, 1, 1, 2, 3, 3, 3, 4, 4))

class ShotRifle(StandardRifle):
    def __init__(self, rounds: int = None, faces: tuple = None):
        if rounds is None:
            rounds = StandardRifle.MAX_ROUNDS-1
        if faces is None:
            faces = (0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4)
        super().__init__(rounds, faces=faces)

class SniperRifle(ShotRifle):
    def __init__(self):
        super().__init__(StandardRifle.MAX_ROUNDS-2, faces=(0, 0, 0, 0, 0, 1, 2, 2, 3, 4, 5, 6))
