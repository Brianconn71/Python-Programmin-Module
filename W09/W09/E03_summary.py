"""Drill. Summarising a column down to one or two numbers.

Run the tests:

    python -m doctest W09/E03_summary.py

No output means every test passed.
"""

import pandas as pd

# Given: the same tiny table as E02.
PENGUINS = pd.DataFrame({
    "species": ["Adelie", "Adelie", "Gentoo", "Gentoo", "Chinstrap"],
    "island": ["Dream", "Biscoe", "Biscoe", "Biscoe", "Dream"],
    "bill_mm": [39.1, 40.3, 46.1, 50.0, 46.5],
    "mass_g": [3750.0, 3250.0, 4500.0, 5700.0, 3500.0],
})


def column_range(df, name):
    """Return (smallest, largest) of one column, as a tuple.

    >>> column_range(PENGUINS, "mass_g")
    (3250.0, 5700.0)
    >>> column_range(PENGUINS, "bill_mm")
    (39.1, 50.0)
    """
    return  # YOUR CODE HERE


def column_mean(df, name):
    """Return the mean of one column, rounded to 2 decimal places.

    >>> column_mean(PENGUINS, "mass_g")
    4140.0
    >>> column_mean(PENGUINS, "bill_mm")
    44.4
    """
    return  # YOUR CODE HERE


def spread(df, name):
    """Return the standard deviation of one column, rounded to 2 places.

    Pandas divides by n - 1, not n, which is the usual convention for a
    sample. Numpy's std divides by n unless you tell it otherwise, so the
    two disagree by a little; this is a famous source of confusion.

    >>> spread(PENGUINS, "bill_mm")
    4.57
    >>> spread(PENGUINS, "mass_g")
    989.57
    """
    return  # YOUR CODE HERE
