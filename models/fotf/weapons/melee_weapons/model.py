from models.fotf.weapons.model import Weapon


class MeleeWeapon(Weapon):
    def __init__(self, rounds: int, max_rounds: int, faces: tuple):
        super().__init__(rounds, max_rounds, faces)

    def attack(self):
        return self._use_weapon()

    def rest(self):
        self._recharge_weapon()
