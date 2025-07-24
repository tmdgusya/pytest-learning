from mycalc.operations import subtract

def test_subtract_positive_numbers():
    assert subtract(10, 3) == 7

def test_subtract_negative_numbers():
    assert subtract(5,8) == -3