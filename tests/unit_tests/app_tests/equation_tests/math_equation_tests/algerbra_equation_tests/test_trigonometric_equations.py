from src.api.builders.equation_builder import build_equation
from src.api.validators.equation_validator import validate_equation


def test_trigonometric_equation():
    sine_eq = build_equation("y(x) = sin(x)")
    validate_equation(sine_eq)

    cosine_eq = build_equation("y(x) = cos(x)")
    validate_equation(cosine_eq)

    tangent_eq = build_equation("y(x) = tan(x)")
    validate_equation(tangent_eq)

