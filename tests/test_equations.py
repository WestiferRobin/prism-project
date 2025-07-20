from src.api.builders.equation_builder import build_equation
from src.api.validators.equation_validator import validate_equation

def test_linear_equations():
    # Basic y = x functions... aka linear
    constant_equation = build_equation("y(x) = c")
    validate_equation(constant_equation)

    linear_equation = build_equation("y(x) = m*x + b")
    validate_equation(linear_equation)


def test_polynomial_equations():
    polynomial_expression = "a*x^2 + b*x + c"

    quadratic_equation = build_equation(f"y(x) = {polynomial_expression}")
    validate_equation(quadratic_equation)

    cubic_equation = build_equation(f"y(t) = {polynomial_expression} + d*x^3")
    validate_equation(cubic_equation)

    root_polynomial_equation = build_equation(f"y(t) = {polynomial_expression} + d*x^(-1/2)")
    validate_equation(root_polynomial_equation)


def test_exponential_equations():
    exponential_growth = build_equation("y(x) = a * e^(b*x)")
    validate_equation(exponential_growth)

    exponential_decay = build_equation("y(t) = a * e^(-b*t)")
    validate_equation(exponential_decay)


def test_logarithmic_equations():
    natural_log = build_equation("y(x) = ln(x)")
    validate_equation(natural_log)

    log_base_b = build_equation("y(x) = log(b, x)")
    validate_equation(log_base_b)


def test_trigonometric_equations():
    sine_eq = build_equation("y(x) = sin(x)")
    validate_equation(sine_eq)

    cosine_eq = build_equation("y(x) = cos(x)")
    validate_equation(cosine_eq)

    tangent_eq = build_equation("y(x) = tan(x)")
    validate_equation(tangent_eq)


def test_rational_equations():
    rational_eq = build_equation("y(x) = (x^2 + 1)/(x - 1)")
    validate_equation(rational_eq)

    rational_quadratic = build_equation("y(x) = (a*x + b)/(c*x^2 + d)")
    validate_equation(rational_quadratic)


def test_absolute_equations():
    abs_eq = build_equation("y(x) = abs(x)")
    validate_equation(abs_eq)

    abs_shifted = build_equation("y(x) = abs(x - 2) + 1")
    validate_equation(abs_shifted)


def test_piecewise_equations():
    piecewise_eq = build_equation("y(x) = {x^2 if x < 0 else 2*x + 1}")
    validate_equation(piecewise_eq)


def test_math_equations():
    test_linear_equations()
    test_polynomial_equations()

    test_exponential_equations()
    test_logarithmic_equations()

    test_trigonometric_equations()
    test_rational_equations()

    test_absolute_equations()
    test_piecewise_equations()


def test_physics_equations():
    distance_equation = build_equation("d(t) = sqrt(x(t)^2 + y(t)^2)")
    validate_equation(distance_equation)

    motion_equation = build_equation("x(t) = x(0) + v(0) * t + (1/2) * a(t) * t^2")
    validate_equation(motion_equation)

    force_equation = build_equation("F(t) = m(t) * a(t)")
    validate_equation(force_equation)

    work_equation = build_equation("W(t) = F(t) * d(t)")
    validate_equation(work_equation)

