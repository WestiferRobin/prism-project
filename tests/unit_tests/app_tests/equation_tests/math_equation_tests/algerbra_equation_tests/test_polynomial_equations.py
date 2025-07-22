from src.api.builders.equation_builder import build_equation
from src.api.validators.equation_validator import validate_equation


def test_polynomial_equation():
    polynomial_expression = "a*x^2 + b*x + c"

    quadratic_equation = build_equation(f"y(x) = {polynomial_expression}")
    validate_equation(quadratic_equation)

    cubic_equation = build_equation(f"y(t) = {polynomial_expression} + d*x^3")
    validate_equation(cubic_equation)

    root_polynomial_equation = build_equation(f"y(t) = {polynomial_expression} + d*x^(-1/2)")
    validate_equation(root_polynomial_equation)

