from lib.high_value import *

def test_initial_values_are_correct():
    high_value = HighValue(6,4)
    assert high_value.value_first == 6
    assert high_value.value_second == 4

def test_first_value_highest():
    high_value = HighValue(6,4)
    high_value.get_highest()
    result = high_value.get_highest()
    assert result == "First value is higher"

def test_second_value_highest():
    high_value = HighValue(3,10)
    high_value.get_highest()
    result = high_value.get_highest()
    assert result == "Second value is higher"

def test_values_are_equal():
    high_value = HighValue(3,3)
    high_value.get_highest()
    result = high_value.get_highest()
    assert result == "Values are equal"

def test_first_value_increased():
    increased_value = HighValue(6,4)
    assert increased_value.add(5, "first") == 11
     
def test_second_value_increased():
    increased_value = HighValue(6,4)
    assert increased_value.add(5, "second") == 9

def test_first_value_increased_by_0():
    increased_value = HighValue(6,4)
    assert increased_value.add(0, "first") == 6
    
def test_second_value_increased_by_zero():
    increased_value = HighValue(6,4)
    assert increased_value.add(0, "second") == 4


