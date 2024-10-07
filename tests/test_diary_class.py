from lib.diary_class import *

def test_class_inits_with_title_and_contents():
    diary_entry = DiaryEntry("Monday", "I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won")
    result_1 = diary_entry.title
    result_2 = diary_entry.contents
    assert result_1 == "Monday"
    assert result_2 == "I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won"

def test_formats_correctly():
    diary_entry = DiaryEntry("Monday", "I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won")
    result = diary_entry.format()
    assert result == "Monday: I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won"

def test_count_words_function():
    diary_entry = DiaryEntry("Monday", "I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won")
    result = diary_entry.count_words()
    assert result == 26

def test_reading_time():
    diary_entry = DiaryEntry("Monday", "I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won")
    result = diary_entry.reading_time(1.5)

def test_reading_chunk():
    diary_entry = DiaryEntry("Monday", "I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won")
    result = diary_entry.reading_chunk(2,3)
    assert result == "I went to class today, it"
    result_2 = diary_entry.reading_chunk(2,3)
    assert result_2 == "was great! We learned a lot"

def test_reading_chunk_2():
    diary_entry = DiaryEntry("Monday", "I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won.")
    result = diary_entry.reading_chunk(2,7)
    assert result == "I went to class today, it was great! We learned a lot about coding"
    result_2 = diary_entry.reading_chunk(2,7)
    assert result_2 == "and other interesting things. Shola and I played Jenga and I won."
    result_3 = diary_entry.reading_chunk(2,3)
    assert result_3 == "I went to class today, it"

def test_reading_chunk_3():
    diary_entry = DiaryEntry("Monday", "I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won.")
    result = diary_entry.reading_chunk(2,7)
    assert result == "I went to class today, it was great! We learned a lot about coding"
    result_2 = diary_entry.reading_chunk(2,7)
    assert result_2 == "and other interesting things. Shola and I played Jenga and I won."
    result_3 = diary_entry.reading_chunk(2,3)
    assert result_3 == "I went to class today, it"
    result_4 = diary_entry.reading_chunk(2,10)
    assert result_4 == "was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won."
    result_5 = diary_entry.reading_chunk(2,5)
    assert result_5 == "I went to class today, it was great! We learned"
    



# def test_reading_chunk_second_call():
#     diary_entry = DiaryEntry("Monday", "I went to class today, it was great! We learned a lot about coding and other interesting things. Shola and I played Jenga and I won")
#     result = diary_entry.reading_chunk(2,3)
#     assert result == "was great! We learned a lot"
