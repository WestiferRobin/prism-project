from src.models.equation import Equation


def validate_expression(expression: str):
    assert expression is not None
    assert type(expression) is str


def validate_equation(equation: Equation):
    assert equation is not None
    assert type(equation) is Equation

    validate_expression(equation.expression)

