from src.api.equations import Equation


class Acceleration(Equation):
    initial_acceleration: float

    def __init__(self,
        initial_acceleration: float = 0,
    ):
        super().__init__(initial_acceleration=initial_acceleration)

    def __str__(self):
        return f"{self.initial_acceleration} "

    def calculate(self, time: float = 0) -> float:
        final_acceleration = self.initial_acceleration
        # TODO: time = i * tau
        return final_acceleration

