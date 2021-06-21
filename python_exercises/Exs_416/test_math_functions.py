from math_functions import fib

def test_fib_basic_initial():
    assert fib(0) == 0
    assert fib(1) == 1

def test_fib_2():
    assert fib(2) == 1

def test_fib_3():
    assert fib(3) == 2

def test_fib_4():
    assert fib(4) == 3

def test_fib_5():
    assert fib(5) == 5

def test_fib_6():
    assert fib(6) == 8

def test_fib_7():
    assert fib(7) == 13

def test_fib_8():
    assert fib(8) == 21