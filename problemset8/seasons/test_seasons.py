from seasons import checkFormat

def test_format():
    assert checkFormat('1999-01-12') == ('1999', '01', '12')
    assert checkFormat('19922-1-12') == None
    assert checkFormat('January 1, 2023') == None

