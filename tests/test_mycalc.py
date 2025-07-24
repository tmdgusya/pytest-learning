
from mycalc.mycalc import add
import pytest

def test_add_positive_numbers():
    a = 2
    b = 3
    expected_result = 5

    actual_result = add(a, b)

    assert actual_result == expected_result

def test_add_negative_numbers():
    a = -5
    b = 3
    expected_result = -2

    actual_result = add(a, b)

    assert actual_result == expected_result

def test_add_type_error():
    with pytest.raises(TypeError):
        add("two", 3)

