"""Drill. Fibonacci from the bottom up.

Run the tests:

    python -m doctest W07/E03_fib_table.py

No output means every test passed.

The lecture's `fib_slow` is exponential because it asks the same questions over
and over. Fill a table instead, smallest first, so each answer is computed
once. Then notice how little of that table you actually needed.
"""
def fib_table(n):
    """Return the nth Fibonacci number, building a list from the bottom up.

    >>> [fib_table(i) for i in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> fib_table(35)
    9227465
    """
    return  # YOUR CODE HERE


def fib_pair(n):
    """The same answer, keeping only the two values we still need.

    >>> [fib_pair(i) for i in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> fib_pair(35)
    9227465
    >>> all(fib_pair(i) == fib_table(i) for i in range(50))
    True
    """
    return  # YOUR CODE HERE


# `fib_table` holds n numbers to return one. `fib_pair` holds two. This is the
# same saving we make for edit distance in E05, one dimension down: look at the
# recurrence, see how far back it actually reaches, and keep only that much.
