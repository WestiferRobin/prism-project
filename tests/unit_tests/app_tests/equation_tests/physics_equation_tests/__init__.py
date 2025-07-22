from api.builders.equation_builder import build_equation
from api.validators.equation_validator import validate_equation


def test_physics_equations():
    motion_equation = build_equation("x(t) = x(0) + v(0) * t + (1/2) * a(t) * t^2")
    validate_equation(motion_equation)

    force_equation = build_equation("F(t) = m(t) * a(t)")
    validate_equation(force_equation)

    gravity_equation = build_equation("F(t) = m(t) * g")
    validate_equation(gravity_equation)

    work_equation = build_equation("W(t) = F(t) * d(t)")
    validate_equation(work_equation)