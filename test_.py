import pytest
from ASD.ASD_lab_Hanoi import moveTower
from ASD.ASD_lab_Fib import Fib

fromPole = str("a")
toPole = str("c")
withPole = str("b")
@pytest.mark.parametrize("height, expected",[(2,3),(3,7),(5,31),(10,1023)])
def test_hanoi(height,expected):
    assert moveTower(height,fromPole,toPole,withPole) == expected
@pytest.mark.parametrize("input, exptected",[(2,2),(3,3),(5,8),(10,89)])
def test_fib(input, exptected):
    assert Fib(input) == exptected