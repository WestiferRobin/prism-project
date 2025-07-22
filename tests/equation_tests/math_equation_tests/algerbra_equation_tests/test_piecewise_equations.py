from api.builders.equation_builder import build_equation
from api.validators.equation_validator import validate_equation


def test_piecewise_equation():
    piecewise_eq = build_equation("y(x) = {x^2 if x < 0 else 2*x + 1}")
    validate_equation(piecewise_eq)

