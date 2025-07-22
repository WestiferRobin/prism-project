from api.builders.equation_builder import build_equation
from api.validators.equation_validator import validate_equation


def test_rational_equation():
    rational_eq = build_equation("y(x) = (x^2 + 1)/(x - 1)")
    validate_equation(rational_eq)

    rational_quadratic = build_equation("y(x) = (a*x + b)/(c*x^2 + d)")
    validate_equation(rational_quadratic)

