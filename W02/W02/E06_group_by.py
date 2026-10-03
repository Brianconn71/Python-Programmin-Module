"""Drill. defaultdict, for collecting rather than counting.

Run the tests:

    python -m doctest W02/E06_group_by.py

No output means every test passed.
"""

from collections import defaultdict


def group_by_first_letter(words):
    """Group words by their first letter, keeping the order they came in.

    Use a defaultdict for this. 
    Return a plain dict, not a defaultdict, so that it prints tidily:
    dict(d) makes an ordinary dict out of any dict.

    >>> group_by_first_letter(["apple", "avocado", "banana"])
    {'a': ['apple', 'avocado'], 'b': ['banana']}
    >>> group_by_first_letter([])
    {}
    >>> group_by_first_letter(["one"])
    {'o': ['one']}
    """
    # defaultdict(list) creates a dictionary which will automatically create an empty list. 
    # The first time a key is used that is not yet in the dictionary
    default = defaultdict(list)
    # loop through the values we are getting from the input
    for word in words:
        # adding the value from the input to the newly created dictionary.
        # The key will be the first letter of the value we are iterating with.
        default[word[0]].append(word)
    # now change the default dictionary back to a plain dictionary and return it to user.
    return dict(default)

