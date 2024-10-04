from lib.grammar_stats import *

def test_bad_grammar():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("oh yeah this sentence is crappy")
    assert result == False

def test_good_grammar():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Oh yeah this sentence is wicked!")
    assert result == True

def test_percentage_of_tests_passed():
    grammar_stats = GrammarStats()

    result1 = grammar_stats.check("oh yeah this sentence is crappy")
    assert result1 == False

    result2 = grammar_stats.check("Oh yeah this sentence is wicked!")
    assert result2 == True

    result3 = grammar_stats.percentage_good()
    assert result3 == 0.5

def test_percentage_of_tests_passed_2():
    grammar_stats = GrammarStats()

    result1 = grammar_stats.check("oh yeah this sentence is crappy")
    assert result1 == False

    result2 = grammar_stats.check("Oh yeah this sentence is wicked!")
    assert result2 == True

    result2 = grammar_stats.check("Oh yeah this sentence is wicked!")
    assert result2 == True

    result2 = grammar_stats.check("Oh yeah this sentence is wicked!")
    assert result2 == True

    result3 = grammar_stats.percentage_good()
    assert result3 == 0.75




