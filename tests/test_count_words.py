from lib.count_words import *

def test_string_with_one_word():
    result = count_words("one")
    assert result == 1

def test_string_with_three_words():
    result = count_words("one two three")
    assert result == 3   

def test_string_with_ten_words():
    result = count_words("one two three four five six seven eight nine ten")
    assert result == 10

def test_string_with_no_words():
    result = count_words("")
    assert result == 0