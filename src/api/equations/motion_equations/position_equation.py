from src.api.equations import Equation
from src.api.equations.motion_equations.acceleration_equation import Acceleration
from src.api.equations.motion_equations.velocity_equation import Velocity


class Position(Equation):
    initial_position: float
    velocity: Velocity
    acceleration: Acceleration

    def __init__(self,
        initial_position: float = 0,
        velocity: Velocity = None,
        acceleration: Acceleration = None
    ):
        if velocity is None:
            velocity = Velocity()
        if acceleration is None:
            acceleration = velocity.acceleration
        super().__init__(
            initial_position=initial_position,
            velocity=velocity,
            acceleration=acceleration
        )

    def calculate(self, time: float) -> float:
        initial_position = self.initial_position
        initial_velocity = self.velocity.calculate(0) * time
        initial_acceleration = 0.5 * self.acceleration.calculate(time) * (time ** 2)
        final_position = initial_position + initial_velocity + initial_acceleration
        return final_position

