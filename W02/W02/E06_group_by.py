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
    #d = defaultdict(list)
    #new_dict = {}
    #l = []
    #for x in words:
    #    if x[0] not in new_dict:
    #        new_dict[x[0]] = [x]
    #    else:
    #        new_dict[x[0]].append(x)
    #    return  new_dict
    # below creates an empty list to each first letter
    # then append adds to it
    default = defaultdict(list)
    for word in words:
        default[word[0]].append(word)
    return dict(default)

