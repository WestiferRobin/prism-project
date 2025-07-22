from src.api.builders.equation_builder import build_equation
from src.api.validators.equation_validator import validate_equation


def test_exponential_equation():
    exponential_growth = build_equation("y(x) = a * e^(b*x)")
    validate_equation(exponential_growth)

    exponential_decay = build_equation("y(t) = a * e^(-b*t)")
    validate_equation(exponential_decay)

