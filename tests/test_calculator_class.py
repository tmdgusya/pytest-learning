
from mycalc.mycalc import add
from mycalc.operations import subtract

class TestCalculator:

    def test_addition_basic(self):
        print("running test_addition_basic")
        assert add(5, 3) == 8

    def test_subtract_basic(self):
        print("running test_subtract_basic")
        assert subtract(5, 3) == 2