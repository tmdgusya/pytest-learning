
import pytest
from mycalc.calculator import Calculator

@pytest.fixture
def calculator_instance():
    calc = Calculator()
    return calc

