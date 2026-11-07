"""Drill. Getting rows and columns out of a table.

Run the tests:

    python -m doctest W09/E02_select.py

No output means every test passed.

A DataFrame is a table: named columns, each holding one kind of thing, and
rows that line up across them. Everything this week starts here.
"""

import pandas as pd

# Given: a tiny table to practise on. Five penguins, four of the columns the
# lecture used.
PENGUINS = pd.DataFrame({
    "species": ["Adelie", "Adelie", "Gentoo", "Gentoo", "Chinstrap"],
    "island": ["Dream", "Biscoe", "Biscoe", "Biscoe", "Dream"],
    "bill_mm": [39.1, 40.3, 46.1, 50.0, 46.5],
    "mass_g": [3750.0, 3250.0, 4500.0, 5700.0, 3500.0],
})


def column_list(df, name):
    """Return one column of df as an ordinary Python list.

    >>> column_list(PENGUINS, "species")
    ['Adelie', 'Adelie', 'Gentoo', 'Gentoo', 'Chinstrap']
    >>> column_list(PENGUINS, "mass_g")
    [3750.0, 3250.0, 4500.0, 5700.0, 3500.0]
    """
    # use the input column name on the inut dataframe to select the column in the dataframe
    # then, use.to_list method on the dataframe column to turn it into a python list
    col_to_list = df[name].to_list()
    # return this python list to the user
    return  col_to_list


def heavier_than(df, grams):
    """Return the rows of df whose mass_g is greater than grams.

    The result is a DataFrame, not a list, so it still has all its columns.

    >>> heavier_than(PENGUINS, 4000)["species"].tolist()
    ['Gentoo', 'Gentoo']
    >>> heavier_than(PENGUINS, 3600)["species"].tolist()
    ['Adelie', 'Gentoo', 'Gentoo']

    Nothing qualifies, and that is an empty table rather than an error:

    >>> len(heavier_than(PENGUINS, 10000))
    0
    """
    # use the input grams argument from user as a conditional on the dataframe column mass_g
    # this will be similar to a loop and compare the grams input against the values in the column and the result heavy will be a pandas series
    # of boolean logic, True or False
    heavy = df["mass_g"] > grams
    # then, use the pandas series on the actual dataframe to return values to user which are heavier than the grams argument.
    return df[heavy]

if __name__ == "__main__":
    heavier_than(PENGUINS, 4000)["species"].tolist()