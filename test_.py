import pytest
from random import randint

from ASD.ASD_1.ASD_lab_Hanoi import moveTower
from ASD.ASD_1.ASD_lab_Fib import Fib

fromPole = str("a")
toPole = str("c")
withPole = str("b")
@pytest.mark.parametrize("height, expected",[(2,3),(3,7),(5,31),(10,1023),(4,15)])
def test_hanoi(height,expected):
    assert moveTower(height,fromPole,toPole,withPole) == expected
@pytest.mark.parametrize("input, exptected",[(2,2),(3,3),(5,8),(10,89)])
def test_fib(input, exptected):
    assert Fib(input) == exptected



from ASD.ASD_2.ASD_lab_sortings import quicksort_func

def gen_and_sort(max_value):
  arr = [randint(0, max_value) for x in range(max_value)]
  return arr, sorted(arr)

@pytest.mark.parametrize("array, expected",[gen_and_sort(100),gen_and_sort(1000),gen_and_sort(10000)])
def test_quicksort_100(array, expected):
    assert quicksort_func(array,0,len(array)-1) == expected
