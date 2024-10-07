from lib.to_do_list_challenge import *
import pytest

def test_adding_task():
    reminder = Reminder("Max")
    reminder.remind_me_to("Do the laundry")
    result = reminder.remind()
    assert result == "Max! Remember to: Do the laundry"

def test_adding_two_tasks():
    reminder = Reminder("Max")
    reminder.remind_me_to("Do the laundry")
    reminder.remind_me_to("walk the dog")
    result = reminder.remind()
    assert result == "Max! Remember to: Do the laundry, walk the dog"

def test_completing_task():
    reminder = Reminder("Max")
    reminder.remind_me_to("Do the laundry")
    reminder.remind_me_to("walk the dog")
    reminder.complete_task("Do the laundry")

    result = reminder.remind()
    assert result == "Max! Remember to: walk the dog"

def test_no_tasks_set():
    reminder = Reminder("Max")
    with pytest.raises(Exception) as error: # <-- New code
        reminder.remind()
    error_message = str(error.value) # <-- New code
    assert error_message == "No tasks set"

def test_empty_task_set():
    reminder = Reminder("Max")
    reminder.remind_me_to("")
    result = reminder.remind()
    assert result == "Max! Remember to: "
    