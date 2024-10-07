# File: lib/diary.py

class Diary:
    def __init__(self):
        self.diary_entries = []

    def add(self, entry):
        self.diary_entries.append(entry)
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        if len(self.diary_entries) == 0:
            raise Exception("No diary entries")
        return self.diary_entries
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        return len(", ".join(self.diary_entries).split())
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        number_of_words = len(", ".join(self.diary_entries).split())
        number_of_minutes = (number_of_words // wpm)
        number_of_seconds = int((number_of_words / wpm) * 60)
        if number_of_minutes == 1:
            return str(number_of_minutes) + " minute " + str((number_of_seconds) - number_of_minutes * 60) + " seconds"
        elif number_of_minutes == 0:
            return str(number_of_seconds) + " seconds"
        elif number_of_minutes > 1:
            return str(number_of_minutes) + " minutes " + str((number_of_seconds) - number_of_minutes * 60) + " seconds"
        # Parameters:
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        max_number_of_words = wpm * minutes
        entry_length = len(", ".join(self.diary_entries).split())
        if len(self.diary_entries) == 0:
            raise Exception("N/A - no diary entries")
        for entry in self.diary_entries:
            if entry_length == max_number_of_words:
                return entry


        
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass
