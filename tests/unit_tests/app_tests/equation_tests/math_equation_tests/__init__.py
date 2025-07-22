from unit_tests.app_tests.equation_tests.math_equation_tests.algerbra_equation_tests import test_algebra_equations
from unit_tests.app_tests.equation_tests.math_equation_tests.test_geometry import test_geometry_equations


def test_math_equations():
    test_algebra_equations()
    test_geometry_equations()

