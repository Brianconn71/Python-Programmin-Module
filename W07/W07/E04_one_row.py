"""Composition. Edit distance in one row.

Run the tests:

    python -m doctest W07/E04_one_row.py

No output means every test passed.

The lecture showed that `D[i][j]` needs only two cells from the row above and
the one immediately to its left. So the whole table is never needed: two lists
are enough, the row we finished and the row we are building.

Your `levenshtein_row` must return exactly what `E01`'s `levenshtein` returns.

**Do not build a table.** The point of the exercise is the space, and a grid of
`(len(a)+1) x (len(b)+1)` cells gives the right answers while missing that
entirely. Nothing here checks. You are on your honour, and the interview is
where it gets asked about.
"""

from E01_editdist import levenshtein
def levenshtein_row(a, b):
    """Edit distance, holding only two rows at a time.

    >>> levenshtein_row("kitten", "sitting")
    3
    >>> levenshtein_row("ACGTACGTAC", "CGTACGTACA")
    2
    >>> levenshtein_row("", "abc")
    3
    >>> levenshtein_row("abc", "abc")
    0
    >>> levenshtein_row("", "")
    0

    It must agree with the lecture's table version everywhere:

    >>> pairs = [("kitten", "sitting"), ("flaw", "lawn"), ("", "abc")]
    >>> all(levenshtein_row(a, b) == levenshtein(a, b) for a, b in pairs)
    True
    """
    # using levenshtein_row("hat", "bat") as an example here
    # below variable prevValue is used to build the top row, b is "bat"
    # so, len(b) + 1 = 4 so essevtially range is going to be [0 ,1, 2, 3]
    prevValue = list(range(len(b) + 1))

    # Loops through the letters in a input, in this case a = "hat"
    # so, len(a) + 1 = 4, eacxh separate loop will build a new row
    for i in range(1, len(a)+ 1):
        # make a new row with loop value i as the first cell
        currentValue = [i]
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            currentValue.append(min(
                prevValue[j] + 1,
                currentValue[j - 1] + 1,
                prevValue[j - 1] + cost
            ))
        prevValue = currentValue
    return prevValue[-1]
   


def levenshtein_row_from_E1(a, b):
    """Edit distance, holding only two rows at a time.

    >>> levenshtein_row_from_E1("kitten", "sitting")
    3
    >>> levenshtein_row_from_E1("ACGTACGTAC", "CGTACGTACA")
    2
    >>> levenshtein_row_from_E1("", "abc")
    3
    >>> levenshtein_row_from_E1("abc", "abc")
    0
    >>> levenshtein_row_from_E1("", "")
    0

    It must agree with the lecture's table version everywhere:

    >>> pairs = [("kitten", "sitting"), ("flaw", "lawn"), ("", "abc")]
    >>> all(levenshtein_row_from_E1(a, b) == levenshtein(a, b) for a, b in pairs)
    True
    """
    return  levenshtein(a, b)

if __name__ == "__main__":
    levenshtein_row("hat", "bat")