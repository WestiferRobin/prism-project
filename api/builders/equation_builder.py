from app.models.equation import Equation


def build_equation(expression: str) -> Equation:
    return Equation(expression=expression)

