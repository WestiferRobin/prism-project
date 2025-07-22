from equation_tests.math_equation_tests.algerbra_equation_tests.test_absolute_equations import test_absolute_equation
from equation_tests.math_equation_tests.algerbra_equation_tests.test_distance_equations import test_distance_equation
from equation_tests.math_equation_tests.algerbra_equation_tests.test_exponential_equations import \
    test_exponential_equation
from equation_tests.math_equation_tests.algerbra_equation_tests.test_linear_equations import test_linear_equation, \
    test_constant_equation
from equation_tests.math_equation_tests.algerbra_equation_tests.test_logarithmic_equations import \
    test_logarithmic_equation
from equation_tests.math_equation_tests.algerbra_equation_tests.test_piecewise_equations import test_piecewise_equation
from equation_tests.math_equation_tests.algerbra_equation_tests.test_polynomial_equations import \
    test_polynomial_equation
from equation_tests.math_equation_tests.algerbra_equation_tests.test_rational_equations import test_rational_equation
from equation_tests.math_equation_tests.algerbra_equation_tests.test_trigonometric_equations import \
    test_trigonometric_equation


def test_basic_algebra_equations():
    test_constant_equation()
    test_linear_equation()
    test_polynomial_equation()
    test_exponential_equation()
    test_rational_equation()
    test_logarithmic_equation()
    test_absolute_equation()


def test_special_algebra_equations():
    test_piecewise_equation()
    test_trigonometric_equation()
    test_distance_equation()


def test_algebra_equations():
    test_basic_algebra_equations()
    test_special_algebra_equations()

