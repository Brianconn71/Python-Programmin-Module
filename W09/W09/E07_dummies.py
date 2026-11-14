"""Drill. Turning words into numbers a distance can be computed on.

Run the tests:

    python -m doctest W09/E07_dummies.py

No output means every test passed.

"Gentoo" is not a number, and there is no sensible distance between it and
"Adelie". One-hot encoding replaces the column with one column per value,
holding 1 where that was the value and 0 everywhere else. The lecture used
this on species and island.
"""

import pandas as pd

# Given: the same tiny table as E02.
PENGUINS = pd.DataFrame({
    "species": ["Adelie", "Adelie", "Gentoo", "Gentoo", "Chinstrap"],
    "island": ["Dream", "Biscoe", "Biscoe", "Biscoe", "Dream"],
    "bill_mm": [39.1, 40.3, 46.1, 50.0, 46.5],
    "mass_g": [3750.0, 3250.0, 4500.0, 5700.0, 3500.0],
})


def encode(df, column):
    """Replace one text column with a 0/1 column for each of its values.

    The new columns are named after the old column and the value, so
    "species" becomes "species_Adelie", "species_Chinstrap", "species_Gentoo".
    Use dtype=int: by default you get True and False, which are the same
    thing but print less clearly.

    >>> out = encode(PENGUINS, "species")
    >>> "species" in out.columns
    False
    >>> [c for c in out.columns if c.startswith("species_")]
    ['species_Adelie', 'species_Chinstrap', 'species_Gentoo']
    >>> out["species_Gentoo"].tolist()
    [0, 0, 1, 1, 0]

    The other columns are left alone:

    >>> out["bill_mm"].tolist()
    [39.1, 40.3, 46.1, 50.0, 46.5]

    And it works on any text column:

    >>> encode(PENGUINS, "island")["island_Dream"].tolist()
    [1, 0, 0, 0, 1]
    """
    # one-hot encoder turns a text column into numbers so maths can be done on it, eg in this case the species column
    # column gets replaced by one column with 0 or 1 values per distinct text value in the column
    # get_dummies is pandas built in one-hot encoder method. takes the input dataframe df and column input to be encoded
    # returns a new dataframe with specified column replaced new values columns, if no column specified then all text columns would be encoded
    # dtype = int ensures values are retuned in the new dataframe for the column as integer values either 0 or 1
    return pd.get_dummies(df, columns=[column], dtype=int)


def n_new_columns(df, column):
    """How many columns would encoding `column` add, net of the one removed?

    One column goes, one per distinct value arrives.

    >>> n_new_columns(PENGUINS, "species")     # 3 species, minus the original
    2
    >>> n_new_columns(PENGUINS, "island")      # 2 islands, minus the original
    1
    """
    # We get length of the input df columns as a value
    columnsInDf = len(df.columns)
    # now reuse the encode function we wrote above to encode the input df with the specified column which encodes the column from text to numbers
    encodedDf = encode(df, column)
    # then, as specifed as the reason for this function.
    # We return to user the difference in the leght of columns in the new encoded df to the columns in the old df
    return len(encodedDf.columns) - columnsInDf



if __name__ == "__main__":
    out = encode(PENGUINS, "species")
    "species" in out.columns
    n_new_columns(PENGUINS, "species") 
# Write it once yourself, then use the built-in for the rest of your life:
# n_new_columns is only ever a sanity check. pandas already knows how wide
# the result is, and encode(df, column).shape[1] will tell you.
