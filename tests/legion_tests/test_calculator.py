import pytest

from tests.legion_tests.calculator import Calculator


@pytest.fixture
def calc():
    """Creates a Calculator instance before each test."""
    return Calculator()

# ✅ Test add method
def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

# ✅ Test subtract method
def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-1, -1) == 0

# ✅ Test multiply method
def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 5) == -10
    assert calc.multiply(0, 100) == 0

# ✅ Test divide method (including error handling)
def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calc.divide(5, 0)  # Expecting an error
