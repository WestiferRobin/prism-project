from src.api.converters.unit_converter import convert_unit
from src.models.equations import Equation
from src.models.equations.motion_equations.acceleration_equation import Acceleration
from src.enums.unit_enums import UnitType
from src.enums.unit_enums.prefix_enums import PrefixType
from src.models.unit import Mass, Unit


class Force(Equation, Unit):
    mass: Mass
    acceleration: Acceleration

    def __init__(self, mass: Mass, acceleration: Acceleration):
        if mass.prefix != PrefixType.KILO:
            mass_value = convert_unit(mass, prefix=PrefixType.KILO)
        else:
            mass_value = mass.amount

        amount = mass_value * acceleration.calculate()
        super().__init__(
            mass=mass,
            acceleration=acceleration,
            amount=amount,
            type=UnitType.NEWTON,
            prefix=PrefixType.NONE
        )

    def to_string(self) -> str:
        return f"F(t) = m(t) * a(t)"

    def calculate(self, t: float = 0) -> float:
        force = self.mass.amount * self.acceleration.calculate(t)
        return force

