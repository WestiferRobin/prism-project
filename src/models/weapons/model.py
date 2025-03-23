import random
from typing import Tuple


class Weapon:
    def __init__(self, points: int, max_points: int, faces: Tuple[int]):
        if points <= 0:
            points = 0
        elif points >= max_points:
            points = max_points
        self.points = points
        self.current_points = self.points
        self.faces = faces

    def can_use(self):
        return self.current_points <= 0

    def _use_weapon(self):
        if not self.can_use():
            return
        weapon_damage = random.choice(self.faces)
        self.current_points -= 1
        return weapon_damage

    def _recharge_weapon(self):
        self.current_points = self.points