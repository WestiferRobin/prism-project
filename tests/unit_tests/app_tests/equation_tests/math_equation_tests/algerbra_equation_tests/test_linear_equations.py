from api.builders.equation_builder import build_equation
from api.validators.equation_validator import validate_equation


def test_constant_equation():
    constant_equation = build_equation("y(x) = c")
    conditions = [
        {
            "x": 1,
            "c": 1,
            "y": 1
        }
    ]
    validate_equation(constant_equation, conditions)


def test_linear_equation():
    linear_equation = build_equation("y(x) = m*x + b")
    conditions = [
        {
            "x": 1,
            "m": 1,
            "b": 0,
            "y": 1
        }
    ]
    validate_equation(linear_equation, conditions)

