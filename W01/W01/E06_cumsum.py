"""Drill. The accumulator pattern.

Run the tests:

    python -m doctest W01/E06_cumsum.py

No output means every test passed.
"""


def cumsum(L):
    """Return the cumulative sum of L. A tuple input still returns a list.

    >>> cumsum([1, 2, 3])
    [1, 3, 6]
    >>> cumsum([5, 5, 5])
    [5, 10, 15]
    >>> cumsum([])
    []
    >>> cumsum([5])
    [5]
    >>> cumsum((5, 5, 5))
    [5, 10, 15]
    """
    # initialize an empty list
    list = []
    # initialize a counter
    count = 0

    # loop through values input
    for value in L:
        # sum up the values added to the counter
        count += value
        # then append to new list
        list.append(count)

    # return the list
    return list
