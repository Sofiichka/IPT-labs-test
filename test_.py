import pytest
from ASD.ASD_lab_Hanoi import moveTower
from ASD.ASD_lab_Fib import Fib

fromPole = str("a")
toPole = str("c")
withPole = str("b")
@pytest.mark.parametrize("height, expected",[(2,3),(3,7),(5,31),(10,1023)])
def test_hanoi(height,expected):
    assert moveTower(height,fromPole,toPole,withPole) == expected
@pytest.mark.parametrize("input, exptected",[()])
def test_fib(input, expected):
    assert Fib(input) == expected