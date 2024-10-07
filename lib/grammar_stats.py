
class GrammarStats:
    def __init__(self):
        self.tests_passed = 0
        self.tests_failed = 0

    def check(self, text):
        capitals_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        punctuation_list = [".", "?", "!"]
        first_letter = text[0]
        last_character = text[-1]
        if first_letter not in capitals_list:
            self.tests_failed += 1
            return False
        elif last_character not in punctuation_list:
            self.tests_failed += 1
            return False
        else:
            self.tests_passed += 1
            return True

    def percentage_good(self):
        return self.tests_passed / (self.tests_passed + self.tests_failed)

        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass
