# test main.py
from src.main import add, subtract

def test_addition():
    assert add(1, 2) == 3

def test_zero():
    assert add(0, 0) == 0

def test_negative_numbers():
    assert add(-1, -1) == -2

def test_mixed_numbers():
    assert add(5, -3) == 2
