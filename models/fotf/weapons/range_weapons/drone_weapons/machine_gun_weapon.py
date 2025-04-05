from models.fotf.weapons.range_weapons.drone_weapons.gun_weapon import Gun


class MachineGun(Gun):
    MAX_ROUNDS = 4
    def __init__(self, rounds: int, faces: tuple):
        super().__init__(rounds, MachineGun.MAX_ROUNDS, faces)


class SMG(MachineGun):
    def __init__(self):
        super().__init__(2, (0, 0, 1, 2, 3, 4))


class LMG(MachineGun):
    super().__init__(4, (0, 0, 2, 3, 4, 5))