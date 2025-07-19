from src.models.equations.force_equations import Force
from src.models.equations.motion_equations.acceleration_equation import Acceleration
from src.models.unit import Mass
from src.utils.constants import EARTH_GRAVITY


class GravityForce(Force):
    def __init__(self, mass: Mass, gravity_amount: float = EARTH_GRAVITY):
        gravity = Acceleration(initial_acceleration=gravity_amount)
        super().__init__(mass, gravity)

    def to_string(self) -> str:
        return f"F(t) = m(t) * g, when g = {self.acceleration}"

