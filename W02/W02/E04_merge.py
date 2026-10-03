"""Drill. Building a new dict instead of changing an old one.

Run the tests:

    python -m doctest W02/E04_merge.py

No output means every test passed.
"""


def merge(d1, d2):
    """Return a new dict with the pairs of both. On a clash, d2 wins.

    Neither argument may be changed.

    >>> merge({"a": 1, "b": 2}, {"a": 17, "c": 3})
    {'a': 17, 'b': 2, 'c': 3}
    >>> merge({}, {"a": 1})
    {'a': 1}

    A doctest runs its lines in order, so we can check afterwards that the
    arguments really were left alone:

    >>> first = {"a": 1, "b": 2}
    >>> second = {"a": 17, "c": 3}
    >>> merge(first, second)
    {'a': 17, 'b': 2, 'c': 3}
    >>> first
    {'a': 1, 'b': 2}
    >>> second
    {'a': 17, 'c': 3}
    """
    # initialize a new dictionary for storing contents of the merge.
    new_dict = {}

    # using .items method to unpack the Dictionaries key and value pair to two searate variables.
    for key, value in d1.items():
        # then adding this to the new Dictionary
        new_dict[key] = value
    # same thing is happening here as above
    for k,v in d2.items():
        # no need for an if statement in this loop because d2 key values will overwrite d1 anyway as its set.
        new_dict[k] = v
    # return the newly created dictionary.
    return  new_dict
