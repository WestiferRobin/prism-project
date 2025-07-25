from zlegacy.api.builders import build_equation
from zlegacy.api.validators import validate_equation


def test_piecewise_equation():
    piecewise_eq = build_equation("y(x) = {x^2 if x < 0 else 2*x + 1}")
    validate_equation(piecewise_eq)

