from models.fotf.weapons.model import Weapon


class RangeWeapon(Weapon):
    def __init__(self, rounds: int, max_rounds: int, faces: tuple):
        super().__init__(rounds, max_rounds, faces)

    def fire(self):
        return self._use_weapon()

    def reload(self):
        self._recharge_weapon()