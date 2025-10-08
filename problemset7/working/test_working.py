from working import convert
import pytest

def test_correct():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'

def test_incorrect():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('9:72 to 6:40')
    with pytest.raises(ValueError):
        convert('9 AM5 PM')
