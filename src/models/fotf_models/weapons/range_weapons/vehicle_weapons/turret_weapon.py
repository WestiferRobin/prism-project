from src.models.fotf_models.weapons import RangeWeapon


class Turret(RangeWeapon):
    MAX_ROUNDS = 3
    def __init__(self, rounds: int = 0):
        super().__init__(rounds, Turret.MAX_ROUNDS)

class LaserTurret(Turret):
    def __init__(self):
        super().__init__(rounds=Turret.MAX_ROUNDS)

class IonTurret(Turret):
    def __init__(self):
        super().__init__(rounds=Turret.MAX_ROUNDS-1)

class MissileTurret(Turret):
    def __init__(self):
        super().__init__(rounds=Turret.MAX_ROUNDS-1)