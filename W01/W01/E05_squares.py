"""Drill. Building a list with append.

Run the tests:

    python -m doctest W01/E05_squares.py

No output means every test passed.
"""


def squares(n):
    """Return a list of the squares of 1 up to and including n.

    >>> squares(4)
    [1, 4, 9, 16]
    >>> squares(1)
    [1]
    >>> squares(0)
    []
    """
    # initialize empty list
    list = []
    # Loop through the values in input list and use range to start at 1. 
    for value in range(1, n+1):
        # Square each value by itself
        valueSquared = value ** 2
        # add the squared value to new list
        list.append(valueSquared)
    # return our new list of squared values.
    return list
