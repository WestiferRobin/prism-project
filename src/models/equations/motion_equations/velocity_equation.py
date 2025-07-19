from src.models.equations import Equation
from src.models.equations.motion_equations.acceleration_equation import Acceleration


class Velocity(Equation):
    initial_velocity: float
    acceleration: Acceleration

    def __init__(self,
                 initial_velocity: float = 0,
                 acceleration: Acceleration = None,
                 ):
        if acceleration is None:
            acceleration = Acceleration()
        super().__init__(
            initial_velocity=initial_velocity,
            acceleration=acceleration
        )

    def to_string(self) -> str:
        return f"v(t) = {self.velocity.initial_velocity} + {self.acceleration.initial_acceleration} * t"

    def calculate(self, t: float = 0) -> float:
        acceleration = self.acceleration.calculate(t)
        final_velocity = self.initial_velocity + acceleration * t
        return final_velocity

