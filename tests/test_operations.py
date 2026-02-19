import pytest
from calculator.operations import add, multiply, divide


def test_add():
    assert add(5, 4) == 8


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
