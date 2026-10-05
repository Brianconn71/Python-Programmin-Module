"""Drill. sorted with a key, and the classic sort bug.

Run the tests:

    python -m doctest W03/E02_sort_by_key.py

No output means every test passed.

QUESTION: why does xs = xs.sort() throw away your list? Write your answer
in the comment at the bottom.
"""


def sort_by_mass(pairs):
    """Sort a list of (name, mass) tuples by mass, lightest first.

    Return a new list. The argument must not be changed.

    >>> sort_by_mass([("frame", 2200), ("spoke", 5), ("tyre", 320)])
    [('spoke', 5), ('tyre', 320), ('frame', 2200)]
    >>> sort_by_mass([])
    []

    >>> parts = [("frame", 2200), ("spoke", 5)]
    >>> sort_by_mass(parts)
    [('spoke', 5), ('frame', 2200)]
    >>> parts
    [('frame', 2200), ('spoke', 5)]
    """
    # result is a variable setup to include the result of calling sorted on the list we take as an argument.
    # It is expected to return a new list of tuples sorted based on the second item in the tuple.
    # lambda is a function that in this case returns the second value in the pair based on the pair we take as argument.
    # sorted essentialy builds a new sorted list based on pairs argument but doesnt change the Pair argument.
    result = sorted(pairs, key=lambda p: p[1])
    # we then return the result which should be a new sorted list based on the original argument without changing that argument.
    return  result


def heaviest(pairs):
    """Return the name of the heaviest part.

    Use max with the same key, rather than sorting and taking the last one.

    >>> heaviest([("frame", 2200), ("spoke", 5), ("tyre", 320)])
    'frame'
    >>> heaviest([("spoke", 5)])
    'spoke'
    """
    # max_result gets the biggest second item in the pair of tuples and returns it as the maximum value.
    # Follows similar logic as sort_by_mass afunction which uses lambda as a small function to return the second item in the pair of tuples
    # this sorts list based on the biggest second value which is what we are expecting and then uses list slicing [0] to return the biggest value
    max_result = max(pairs, key=lambda p: p[1])[0]
    # then return the value we found using list slicing as the maximum value.
    return  max_result


# ANSWER: (the QUESTION is at the top of this file)
# .sort() throws away the list as it has already done its work in place.
# It returns None as a result.
