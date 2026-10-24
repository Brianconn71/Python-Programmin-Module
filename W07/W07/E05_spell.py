"""Composition. Spelling suggestions.

Run the tests:

    python -m doctest W07/E05_spell.py

No output means every test passed.

A spellchecker offers the dictionary words closest to what you typed. That is
edit distance, run once for every word in the dictionary. A real word list has
100,000 entries, which is why we wanted the cheap version in E04: once your
`levenshtein_row` works, it drops straight in here.

QUESTION: `suggest` sorts on `(distance, word)` rather than on `distance`
alone. What would change if it sorted on `distance` alone, and is that a
problem with the function or only with the test? Write your answer in the
comment at the bottom.
"""

from E01_editdist import levenshtein

# Given: a small word list, so the doctests need no real dictionary.
WORDS = ["cat", "cart", "car", "cast", "case", "bat", "dog"]


def suggest(word, words, n=3):
    """Return the n words closest to `word`, nearest first.

    >>> suggest("cet", WORDS)
    ['cat', 'bat', 'car']
    >>> suggest("dat", WORDS)
    ['bat', 'cat', 'car']
    >>> suggest("cat", WORDS, n=1)
    ['cat']
    >>> suggest("cat", [])
    []
    """
    # initialize a variable to store words based in as a key and then the levenshtein distance value as the value
    # storing as a dictionary
    temp_dict = {}

    # Loop through the values in the WORDS input list
    for value in words:
        # Calling the levenshtein fucntion from e1 to calculate the editing distance from the word
        # added as input to function with the WORDS list stored in file.
        # then, we store this as a key pair value in out new dictionary to be used for sorting later
        temp_dict[value] = levenshtein(word, value)

    # Sort the keys in the dict, to do this we run sorted method on the temp_dict
    # and we use the key for sorting as a lambda function which returns a tuple of the word itself and its distance then python looks inside the tuple and compares the items
    # if first items are different then smaller distance comes first and if equal then sort by words themselves so bat will come ahead of car in this instance.
    sortedDictKeys = sorted(temp_dict, key=lambda keyValue: (temp_dict[keyValue], keyValue))

    # finally, return a liced list with the n value added as input to the function
    # this will return the values from the list up to the n value so if n = 3 then return list [0, 1, 2]
    return sortedDictKeys[:n]

if __name__ == "__main__":
    suggest("cet", WORDS)

# ANSWER: (the QUESTION is at the top of this file)
