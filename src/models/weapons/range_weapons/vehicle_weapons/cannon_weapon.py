from src.models.weapons import RangeWeapon


class Cannon(RangeWeapon):
    MAX_ROUNDS = 4
    def __init__(self, rounds: int = 0):
        super().__init__(rounds, Cannon.MAX_ROUNDS)

class LaserCannon(Cannon):
    def __init__(self):
        super().__init__(rounds=Cannon.MAX_ROUNDS)

class IonCannon(Cannon):
    def __init__(self):
        super().__init__(rounds=Cannon.MAX_ROUNDS-1)

class PlasmaCannon(Cannon):
    def __init__(self):
        super().__init__(rounds=Cannon.MAX_ROUNDS-2)
