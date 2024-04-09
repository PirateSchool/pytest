import pytest
from cal import Calculator

# Fixture for creating a calculator instance
@pytest.fixture
def calculator():
    return Calculator()

# Parameterized test for addition
@pytest.mark.parametrize("a, b, expected", [(10, 5, 15), (3, 2, 5), (0, 0, 0)])
def test_add(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

# Test for subtraction
def test_subtract(calculator):
    assert calculator.subtract(10, 5) == 5

# Test for multiplication
def test_multiply(calculator):
    assert calculator.multiply(3, 4) == 12

# Test for division
def test_divide(calculator):
    assert calculator.divide(10, 2) == 5

# Test division by zero
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError) as e:
        calculator.divide(10, 0)
    assert str(e.value) == "Cannot divide by zero."

