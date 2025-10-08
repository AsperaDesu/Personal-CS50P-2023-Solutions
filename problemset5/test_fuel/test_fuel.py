import pytest
from fuel import gauge, convert

def test_fraction():
    assert convert('1/3') == 33
    assert convert('1/2') == 50
    assert convert('0/4') == 0
    assert convert('4/4') == 100

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(100) == 'F'
    assert gauge(33) == '33%'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_value():
    with pytest.raises(ValueError):
        convert('h/q')
