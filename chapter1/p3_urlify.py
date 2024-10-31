# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

def urlify_pythonic(stringa, length):
    return stringa[:length].replace(" ", "%20")

def urlify(string, length):
    # Python ha le stringhe immutabili quindi dobbiamo convertire la stringa in un altro tipo per poterci lavorare, possiamo usare le liste
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return "".join(char_list[new_index:])

print(urlify_pythonic("Mr John Smith    ", 13))
print(urlify("Mr John Smith    ", 13))