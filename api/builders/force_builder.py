from app.models.equation import Equation
from app.models.equations.physics import Force


def build_force(equation: Equation) -> Force:
    return Force(equation=equation)


def build_newton_gravity_force() -> Force:
    force_equation = Equation(expression="F(t) = m(t) * g")
    return build_force(force_equation)

