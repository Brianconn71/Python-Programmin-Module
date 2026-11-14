"""Extension. Each algorithm on the other one's data.

Run the tests:

    python -m doctest W07/E06_wrong_tool.py

No output means every test passed.

Levenshtein is for symbols and DTW is for numbers. Nothing stops you running
either on the other kind of data, and what goes wrong is worth understanding:
each algorithm has an assumption built into it, and the assumption only shows
itself when it is false.

Write both functions, then answer the questions from what the doctests show.

QUESTION 1: `levenshtein` compares items with `==`, and two measured floats are
almost never exactly equal. What does the distance degenerate to? Does `tol`
really fix it?

QUESTION 2: `dtw_symbols("bookkeeper", "bokeper")` is 0.0, meaning DTW calls
the misspelling a perfect match. Explain why, and say whether DTW could ever be
used for spellchecking. Write your answers in the comments at the bottom.
"""

INF = float("inf")


def levenshtein_tol(a, b, tol):
    """Edit distance on numbers, counting two values equal if within tol.

    >>> levenshtein_tol([1.0, 2.0, 3.0], [1.0, 2.0, 3.0], 0.0)
    0
    >>> levenshtein_tol([1.0, 2.0, 3.0], [1.05, 2.0, 3.0], 0.0)
    1
    >>> levenshtein_tol([1.0, 2.0, 3.0], [1.05, 2.0, 3.0], 0.1)
    0
    >>> levenshtein_tol([1.0, 2.0, 3.0], [1.0, 1.0, 2.0, 3.0], 0.1)
    1
    >>> levenshtein_tol([1.0], [999.0], 0.1)
    1
    """
    # This function builds a table of distances betwden each and every prefxi of input a abd b. 
    # The final distance which is asked as the return value is the bottom right corner of the table.
    
    # Creates a grid/table of zeros based on the lngth of input a + b plus 1. The + 1 is used to account for the empty prefix of a and b
    # which means row 0 is 0 items of a and columns is 0 items of b.
    # list comprehension is used to make each row a separate list
    D = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    # fill in the first column with the distance of the empty prefix of b to the prefix in a.
    # thus, the first i items of a to the empty prefix of b is i as it takes i deletions to get from the first i itemsof a to empty prefix b
    for i in range(len(a) + 1):
        D[i][0] = i
    # follows same logic as above but instead uses rows rather than columns to fill 
    for j in range(len(b) + 1):
        D[0][j] = j
    # below loops fill in the remainder of the table, row by row from left to right and start at 1 as 0 is already filled
    # this order ensures that values in cell above, to the left and diagonally to the left are always finished first
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            # compare the newest item in each prefix
            # a[i - 1] & b[j - 1] are the extra empty rows and columns which shift everything by one so as an example
            # row i corresponds to list position i - 1
            # abs gets the absolute difference between two values and turns a negative into a positive value
            # <= tol checks if gap is within the tolerance, if yes cost is nothing if not cost is 1
            cost = 0 if abs(a[i - 1] - b[j - 1]) <= tol else 1
            # D[i-1][j] + 1 i-1 is already turned into a row index so now delete a's new item
            # D[i][j-1] + 1 j-1 is already turned into a column index so now insert b's new item which will cost 1
            # D[i-1][j-1] + cost i -1 and j - 1 are already turned into row and column values so now substitute a's new item for b's or keep it if the cost is 0
            D[i][j] = min(D[i -1][j] + 1,
                            D[i][j -1] + 1,
                            D[i - 1][j - 1] + cost)
    # return the bottom right cell which uses all a and b  so -1 means the last possible value.
    return D[-1][-1]


def dtw_symbols(a, b):
    """DTW on symbols, costing 0 for a match and 1 for a mismatch.

    >>> dtw_symbols("abc", "abc")
    0.0
    >>> dtw_symbols("abc", "xyz")
    3.0
    >>> dtw_symbols("aab", "ab")
    0.0
    >>> dtw_symbols("bookkeeper", "bokeper")
    0.0
    """
    D = [[INF] * (len(b) + 1) for _ in range(len(a) + 1)]
    D[0][0] = 0.0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            D[i][j] = cost + min(D[i - 1][j],
                                 D[i][j - 1],
                                 D[i - 1][j - 1])
    return D[-1][-1]


# ANSWER 1: with tol = 0 every comparison of measured floats fails, so every
# cost is 1 and the distance stops depending on the values at all --- 1.0
# against 1.05 scores the same as 1.0 against 999.0. `tol` restores a little of
# the meaning, but only a little: it turns a distance into a yes-or-no at one
# arbitrary threshold, and 1.0 against 1.05 still scores the same as 1.0
# against 999.0 once both are outside it. DTW's `abs(x - y)` keeps the
# magnitude, which is the whole reason it exists.

# ANSWER 2: DTW has no deletion. Going down or right reuses a value rather than
# dropping it, so a repeated letter is free: the second "o" of "bookkeeper"
# matches the single "o" of "bokeper" at no cost, and likewise for "kk" and
# "ee". DTW therefore cannot see doubled letters at all, which is exactly the
# mistake spellcheckers most need to catch. It is the wrong tool here, and not
# because it is worse --- being blind to a held note is what makes it right for
# a time series.

if __name__ == "__main__":
    levenshtein_tol([1.0], [999.0], 0.1)
    dtw_symbols("bookkeeper", "bokeper")
