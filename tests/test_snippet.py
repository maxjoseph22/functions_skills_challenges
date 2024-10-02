from lib.snippet import *

def test_string_of_six_words():
    result = snippet("one two three four five six")
    assert result == "one two three four five ..."

def test_string_of_eight_words():
    result = snippet("one two three four five six seven eight")
    assert result == "one two three four five ..."

def test_string_of_four_words():
    result = snippet("one two three four")
    assert result == "one two three four"