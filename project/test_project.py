import pytest
from project import convertToMinute, matchList, searchPage
import wikipediaapi

wiki = wikipediaapi.Wikipedia('Project (asperadesu@gmail.com)', 'en')

def test_convertToMinute():
    assert convertToMinute(150000) == ('2', '30')
    assert convertToMinute(105000) == ('1', '45')
    assert convertToMinute(184000) == ('3', '04')


def test_matchList():
    assert matchList(['a'], ['abc', 'jed', 'xyz']) == True
    assert matchList(['music', 'project', 'band'], ['jpop', 'east music', 'metal']) ==  True
    assert matchList(['music', 'project', 'band'], ['ancient', 'scientific', 'relativity']) == False


def test_searchPage():
    keywords = ['musician', 'musical artist', 'singer', 'band','artist','music']
    #testing whether the function actually denies a wiki page that doesn't directly refer to the artist aka a page that has the same name as the artist

    assert searchPage('tsukuyomi', keywords) is None
    #tsukuyomi spotify-wise is actually an username for an underground artist/singer from japan. but if we search her name in wikipedia the page that pops up is the "moon god" tsukuyomi not "singer" tsukuyomi


    assert searchPage('weeknd', keywords) is not None
    assert searchPage('justin beiber', keywords) is not None

