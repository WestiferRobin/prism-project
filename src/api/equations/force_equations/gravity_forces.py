from src.api.equations.force_equations import Force
from src.api.equations.motion_equations.acceleration_equation import Acceleration
from src.models.unit import Mass
from src.utils.constants import EARTH_GRAVITY


class GravityForce(Force):
    def __init__(self, mass: Mass):
        gravity = Acceleration(initial_acceleration=EARTH_GRAVITY)
        super().__init__(mass, gravity)

