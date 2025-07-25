from zlegacy.api.builders import build_equation
from zlegacy.api.validators import validate_equation


def test_trigonometric_equation():
    sine_eq = build_equation("y(x) = sin(x)")
    validate_equation(sine_eq)

    cosine_eq = build_equation("y(x) = cos(x)")
    validate_equation(cosine_eq)

    tangent_eq = build_equation("y(x) = tan(x)")
    validate_equation(tangent_eq)

