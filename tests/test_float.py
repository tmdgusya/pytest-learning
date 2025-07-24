import pytest

def test_approx():
    assert (0.1 + 0.2) == pytest.approx(0.3)
    assert (1 / 3) == pytest.approx(1 / 3)