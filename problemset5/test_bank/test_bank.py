from bank import value

def test_str():
    assert value('howdy') == 20
    assert value('hOlLa') == 20

def test_hello():
    assert value('Hello') == 0
    assert value('HELLO') == 0

def test_other():
    assert value('123') == 100
    assert value('!@#%') == 100
    assert value('bonjour') == 100
