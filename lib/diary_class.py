class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words_read_count = 0
       
    def format(self):
        return self.title + ": " + self.contents

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        number_of_words = len(self.contents.split())
        number_of_minutes = (number_of_words // wpm)
        number_of_seconds = int((number_of_words / wpm) * 60)
        if number_of_minutes == 1:
            return str(number_of_minutes) + " minute " + str((number_of_seconds) - number_of_minutes * 60) + " seconds"
        elif number_of_minutes == 0:
            return str(number_of_seconds) + " seconds"
        elif number_of_minutes > 1:
            return str(number_of_minutes) + " minutes " + str((number_of_seconds) - number_of_minutes * 60) + " seconds"
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        words_to_read = wpm * minutes
        passage = " ".join((self.contents.split()[self.words_read_count:words_to_read + self.words_read_count]))
        self.words_read_count += words_to_read
        return passage


        # split_contents = self.contents.split()
        # reading_chunk = []
        # for word in split_contents:
        #     reading_chunk.append(word[words_read_count: ])

        # return split_contents
        
    
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass
