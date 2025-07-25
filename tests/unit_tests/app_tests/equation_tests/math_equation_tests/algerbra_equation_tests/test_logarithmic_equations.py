from zlegacy.api.builders import build_equation
from zlegacy.api.validators import validate_equation


def test_logarithmic_equation():
    natural_log = build_equation("y(x) = ln(x)")
    validate_equation(natural_log)

    log_base_b = build_equation("y(x) = log(b, x)")
    validate_equation(log_base_b)

