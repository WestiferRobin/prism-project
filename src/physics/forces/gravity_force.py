from src.physics.forces import Force
from src.utils.constants import GRAVITY

class GravityForce(Force):
    def __init__(self, mass: callable, dim: int = 2):
        gravity_vector = [lambda t: 0.0] * (dim - 1) + [lambda t: -GRAVITY]
        super().__init__(mass, gravity_vector)