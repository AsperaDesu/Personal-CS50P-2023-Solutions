from plates import is_valid

def test_str():
    assert is_valid('HELLO') is True
    assert is_valid('HELLO, WORLD') is False
    assert is_valid('GOODBYE') is False

def test_mixed():
    assert is_valid('CS50') is True
    assert is_valid('CS05') is False
    assert is_valid('PI3.14') is False
    assert is_valid('CS50P') is False
    assert is_valid('OUTATIME') is False

def test_int():
    assert is_valid('50') is False