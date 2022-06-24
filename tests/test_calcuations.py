from app.calculations import add, subract, multiply, divide
import pytest

@pytest.mark.parametrize("num1, num2, expected", [
    (3,5,8),
    (15,16,31),
    (70,56,126)
])
def test_add(num1, num2, expected):
    assert add(num1, num2)==expected

def test_subract():
    assert subract(9,3)==6

def test_multiply():
    assert multiply(9,3)==27

def test_divide():
    assert divide(9,3)==3

