
from mycalc.calculator import Calculator
import pytest

def test_add(calculator_instance):
    assert calculator_instance.add(1, 2) == 3

def test_sub(calculator_instance):
    assert calculator_instance.sub(2, 2) == 0

def test_div(calculator_instance):
    assert calculator_instance.div(1, 2) == 0.5