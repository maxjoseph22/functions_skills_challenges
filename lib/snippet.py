
def snippet(string):
    split_string = string.split()
    if len(split_string) > 5:
        return " ".join(split_string[0:5]) + " ..."
    else:
        return " ".join(split_string)
    