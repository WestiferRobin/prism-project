from zlegacy.api.builders import build_equation
from zlegacy.api.validators import validate_equation


def test_absolute_equation():
    abs_eq = build_equation("y(x) = abs(x)")
    validate_equation(abs_eq)

    abs_shifted = build_equation("y(x) = abs(x - 2) + 1")
    validate_equation(abs_shifted)

