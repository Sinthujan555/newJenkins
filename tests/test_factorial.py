import pytest
from app import factorial

def test_factorial_zeros():
    assert factorial.factorial(0) ==0
def test_factorial_function1():
    assert factorial.factorial(2) ==2
def test_reverse_factorial():
    assert factorial.reverse_factorial(120) ==5

