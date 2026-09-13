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
    vowels = ["a","e","i","o","u"]
    count = 0
    for x in s.lower():
        if x in vowels:
            count += 1
    return count


"""
def count_vowels(s):
    Return the number of vowels in s. Upper case counts too.

     count_vowels("hello")
    2
     count_vowels("xyz")
    0
     count_vowels("AEIOU")
    5
    count_vowels("")
    0
    
    vowels = set("aeiou")
    return sum(1 for x in s.lower() if x in vowels)

    Two small improvements here:

set("aeiou") gives O(1) membership checks instead of O(n) list scans (matters more on long strings/many calls).
s.lower() once up front, rather than calling .lower() on every character.
"""
