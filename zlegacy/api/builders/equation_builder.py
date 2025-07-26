from zlegacy.models import Equation


def build_equation(expression: str) -> Equation:
    return Equation(expression=expression)

