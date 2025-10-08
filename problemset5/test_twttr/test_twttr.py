from twttr import shorten

def test_vowel():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('AMsIong') == 'Msng'

def test_number():
    assert shorten('1234') == '1234'

def test_punct():
    assert shorten('!@#?%') == '!@#?%'
