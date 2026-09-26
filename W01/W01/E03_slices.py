"""Drill. Slicing.

Run the tests:

    python -m doctest W01/E03_slices.py

No output means every test passed.
"""


def middle(s):
    """Return everything except the first and last item.

    >>> middle("hello")
    'ell'
    >>> middle("ab")
    ''
    >>> middle([1, 2, 3, 4])
    [2, 3]
    """
    # slice the list based on excluding first and last item
    everythingElse = s[1:-1]
    return  everythingElse


def last_three(s):
    """Return the last three items. If there are fewer, return them all.

    >>> last_three("hello")
    'llo'
    >>> last_three("hi")
    'hi'
    >>> last_three([1, 2, 3, 4, 5])
    [3, 4, 5]
    """
    # Slice list and return last three items
    lastThree = s[-3:]
    return  lastThree
