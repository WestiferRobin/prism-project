from src.api.equations import Equation
from src.api.equations.motion_equations.acceleration_equation import Acceleration
from src.enums.unit_enums import UnitType
from src.enums.unit_enums.prefix_enums import PrefixType
from src.models.unit import Mass, Unit


class Force(Equation, Unit):
    mass: Mass
    acceleration: Acceleration

    def __init__(self, mass: Mass, acceleration: Acceleration):
        amount = mass.value * acceleration.calculate()
        super().__init__(
            mass=mass,
            acceleration=acceleration,
            amount=amount,
            type=UnitType.NEWTON,
            prefix=PrefixType.NONE
        )

    def calculate(self, time: float = 0) -> float:
        force = self.mass.amount * self.acceleration.calculate(time)
        return force

    def __repr__(self):
        return super(Unit).__str__()

