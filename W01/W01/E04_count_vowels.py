"""Drill. Looping over a string.

Run the tests:

    python -m doctest W01/E04_count_vowels.py

No output means every test passed.
"""


def count_vowels(s):
    """Return the number of vowels in s. Upper case counts too.

    >>> count_vowels("hello")
    2
    >>> count_vowels("xyz")
    0
    >>> count_vowels("AEIOU")
    5
    >>> count_vowels("")
    0
    """
    # list of vowels
    vowels = ["a","e","i","o","u"]
    # initialize a count variable as 0
    count = 0

    # for loop going through input argument and changing each value to lower so to have all letters in one format
    for value in s.lower():
        # if the value is in our vowels list then add to our count variable
        if value in vowels:
            count += 1
    # return the count once loop has walked through the input values.
    return count
