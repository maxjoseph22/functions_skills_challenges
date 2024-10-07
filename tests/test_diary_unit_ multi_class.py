from lib.diary_entry_multi import *
import pytest

def test_add_entry_function():
    diary = Diary()
    diary.add("This is my first diary entry")
    
def test_all_function():
    diary = Diary()
    diary.add("This is my first diary entry")
    result = diary.all()
    assert result == ["This is my first diary entry"]

def test_exception_no_diary_entries():
    diary = Diary()
    with pytest.raises(Exception) as error: 
        diary.all()
    error_message = str(error.value) 
    assert error_message == "No diary entries"

def test_count_words_with_no_entries():
    diary = Diary()
    result = diary.count_words()
    assert result == 0

def test_count_words_with_one_entry():
    diary = Diary()
    diary.add("This is my first diary entry")
    result = diary.count_words()
    assert result == 6

def test_count_words_with_multiple_entries():
    diary = Diary()
    diary.add("This is my first diary entry")
    diary.add("This is my second diary entry")
    result = diary.count_words()
    assert result == 12

def test_reading_time_with_no_entries():
    diary = Diary()
    result = diary.reading_time(4)
    assert result == "0 seconds"

def test_reading_time_with_multiple_entries():
    diary = Diary()
    diary.add("This is my first diary entry")
    diary.add("This is my second diary entry")
    result = diary.reading_time(4)
    assert result == "3 minutes 0 seconds"

def test_best_entry_to_read_no_entries():
    diary = Diary()
    with pytest.raises(Exception) as error:
        diary.find_best_entry_for_reading_time(2,3)
    error_message = str(error.value)
    assert error_message == "N/A - no diary entries"

def test_best_entry_to_read_multiple_entries():
    diary = Diary()
    diary.add("This is my first diary entry")
    diary.add("This is my second diary entry, it's a bit longer than the first!")
    result = diary.find_best_entry_for_reading_time(3,2)
    assert result == "This is my first diary entry"