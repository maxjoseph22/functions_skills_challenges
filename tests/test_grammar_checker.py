from lib.grammar_checker import *

def test_one_word_no_grammar():
    result = grammar_checker("word")
    assert result == False

def test_one_word_capital_no_grammar():
    result = grammar_checker("Word")
    assert result == False

def test_one_word_capital_with_grammar():
    result = grammar_checker("Word.")
    assert result == True

def test_two_word_capital_no_grammar():
    result = grammar_checker("Word word")
    assert result == False

def test_long_string_with_grammar():
    result = grammar_checker("Complete sentence with loads of correct grammar, very important you know!")
    assert result == True   

def test_some_words_with_weird_caps_and_grammar():
    result = grammar_checker("here is a Sentence with some! weird? Grammar")
    assert result == False