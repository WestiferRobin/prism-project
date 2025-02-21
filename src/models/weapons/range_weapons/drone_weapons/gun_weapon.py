from src.models.weapons.range_weapons.model import RangeWeapon


class Gun(RangeWeapon):
    def __init__(self, rounds: int, max_rounds: int, faces: tuple):
        super().__init__(rounds, max_rounds, faces)
