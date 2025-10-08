from um import count

def test_correct():
    assert count('um?') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2

def test_mistake():
    assert count('yummy') == 0
    assert count('yumeuejaef') == 0
