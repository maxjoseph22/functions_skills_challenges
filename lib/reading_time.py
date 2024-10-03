# # {{PROBLEM}} Function Design Recipe

# Copy this into a `recipe.md` in your project and fill it out.

# ## 1. Describe the Problem

# # As a user
# # So that I can manage my time
# # I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

# _Put or write the user story here. Add any clarifying notes you might have._

# ## 2. Design the Function Signature

# def reading_time(string_of_text):

#     # parameters: a string of text

#     # returns: an integer or string representing reading time in seconds or minutes or hours or all of them somehow

#     # side effects: none



# ## 3. Create Examples as Tests

# _Make a list of examples of what the function will take and return._

# given a string of text containing 200 words, the function returns the string "1 minute" 

# given a string of text containing 400 words, the function returns the string "2 minutes"

# given a string of text containing 100 words, the function returns the string "30 seconds"







# ## 4. Implement the Behaviour

# _After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

# Here's an example for you to start with:

def reading_time(string_of_words):
    number_of_words = len(string_of_words.split())
    number_of_minutes = (number_of_words // 200)
    number_of_seconds = int((number_of_words / 200) * 60)
    if number_of_minutes == 1:
        return str(number_of_minutes) + " minute " + str((number_of_seconds) - number_of_minutes * 60) + " seconds"
    elif number_of_minutes == 0:
        return str(number_of_seconds) + " seconds"
    elif number_of_minutes > 1:
        return str(number_of_minutes) + " minutes " + str((number_of_seconds) - number_of_minutes * 60) + " seconds"






# ```python
# # EXAMPLE

# from lib.extract_uppercase import *

# """
# Given a lower and an uppercase word
# It returns a list with the uppercase word
# """
# def test_extract_uppercase_with_upper_then_lower():
#     result = extract_uppercase("hello WORLD")
#     assert result == ["WORLD"]
# ```

# Ensure all test function names are unique, otherwise pytest will ignore them!
