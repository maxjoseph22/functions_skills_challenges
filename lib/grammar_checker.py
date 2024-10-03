
def grammar_checker(string_of_text):
    capitals_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    punctuation_list = [".", "?", "!"]
    first_letter = string_of_text[0]
    last_character = string_of_text[-1]
    if first_letter not in capitals_list:
        return False
    elif last_character not in punctuation_list:
        return False
    else:
        return True
    

