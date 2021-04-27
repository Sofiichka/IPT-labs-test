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
@pytest.mark.parametrize("input, exptected",[(2,2),(3,3),(5,24),(6,132)])
def test_fib(input, exptected):
    assert Fib(input) == exptected



from ASD.ASD_2.ASD_lab_sortings import quicksort_func, buble_sort_func

def gen_and_sort(max_value):
  arr = [randint(0, max_value) for x in range(max_value)]
  return arr, sorted(arr)

@pytest.mark.parametrize("array, expected",[gen_and_sort(100),gen_and_sort(1000),gen_and_sort(10000)])
def test_quicksort(array, expected):
    assert quicksort_func(array,0,len(array)-1) == expected

@pytest.mark.parametrize("array, expected",[gen_and_sort(100),gen_and_sort(1000),gen_and_sort(10000)])
def test_bublesort(array, expected):
    assert buble_sort_func(array) == expected



from ASD.ASD_4.ASD_DEF_QUEUE import Queue

def test_default_queue():
    main = Queue()
    main.push(65)
    assert main.arr[0] == 65

def test_default_queue_fails_on_pulled_element():
    main = Queue()
    main.push(0)
    main.push(1)
    try:
        main.pull()
        assert False
    except Exception:
        assert True

from ASD.ASD_4.ASD_CYCLED_QUEUE import Queue as CycledQueue

def test_Cycled_queue():
    main = CycledQueue()
    main.push(65)
    assert main.arr[0] == 65

def test_Cycled_queue_fails_on_pulled_element():
    main = CycledQueue()
    main.push(0)
    main.push(1)
    try:
        main.pull()
        assert False
    except Exception:
        assert True