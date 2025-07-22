from api.builders.equation_builder import build_equation
from api.validators.equation_validator import validate_equation


def test_logarithmic_equation():
    natural_log = build_equation("y(x) = ln(x)")
    validate_equation(natural_log)

    log_base_b = build_equation("y(x) = log(b, x)")
    validate_equation(log_base_b)

