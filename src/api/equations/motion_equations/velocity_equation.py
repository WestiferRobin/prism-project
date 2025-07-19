
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

    def calculate(self, time: float) -> float:
        acceleration = self.acceleration.calculate(time)
        final_velocity = self.initial_velocity + acceleration * time
        return final_velocity

