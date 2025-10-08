from numb3rs import validate

def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'1000.255.255.255') == False
    assert validate(r'255.1000.255.255') == False
    assert validate(r'255.255.1000.255') == False
    assert validate(r'255.255.255.1000') == False
    assert validate(r'75.456.76.65') == False

def test_format():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False

def test_correct():
    assert validate(r'127.0.0.1') == True
    assert validate(r'255.255.255.255') == True

def test_mistake():
    assert validate(r'512.512.512.512') == False
    assert validate(r'1.2.3.1000') == False
    assert validate(r'cat') == False

