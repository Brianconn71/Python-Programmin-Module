"""Drill. Adding arrays whose shapes do not match.

Run the tests:

    python -m doctest W08/E03_broadcast.py

No output means every test passed.

Numpy stretches a length-1 axis to fit, so a column of 4 and a row of 4 add
up to a 4 by 4 table. Nothing is copied: the stretching is a fiction Numpy
maintains while it reads the values.

Each function below should be one line of Numpy, with no loop.

QUESTION: in combine, c can be added just as it comes, but b cannot. Why
does one of them need reshaping and the other does not?
Answer in the comment at the bottom.
"""
import numpy as np

# Needed to add this line as was having issues with numpy versions
# I had numpy 2.5 installed, newer numpy does not need np.int64(1)
np.set_printoptions(legacy="1.25")


def combine(A, b, c, d):
    """Build the table z, where

        z[i, j] = A[i, j] + b[i] + c[j] + d

    A is 2-D with n rows and m columns, b has n entries, c has m entries,
    and d is a single number.

    >>> A = np.zeros((4, 4))
    >>> b = np.array([10.0, 20.0, 30.0, 40.0])
    >>> c = np.array([1.0, 2.0, 3.0, 4.0])
    >>> combine(A, b, c, 100.0)
    array([[111., 112., 113., 114.],
           [121., 122., 123., 124.],
           [131., 132., 133., 134.],
           [141., 142., 143., 144.]])
    >>> A = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    >>> combine(A, np.array([0.0, 10.0]), np.array([0.0, 0.0, 100.0]), 1.0)
    array([[  2.,   3., 104.],
           [ 15.,  16., 117.]])
    """
    # A is the full shape, full table it has rows and columns
    # b.reshape(-1, 1) turns b into correct format of  (n, 1) for rows and columns, -1 is lazy and asks to work out columns for it
    # c has a shape of (4,) which Numpy treats as a row, c[j] is in column [j]and numpy copies this down all n rows
    # d is a single number which then gets added to each cell
    # using this z then gets A[i, j] + b[i] + c[j] + d, if b was not reshapen then 
    # b would be added as columns instead of rows 
    z = A + b.reshape(-1, 1)+ c + d
    # Once z is correct we return to user 
    return z


def times_table(n):
    """Return the n by n multiplication table.

    Make a row 1, 2, ..., n and a column of the same numbers, and multiply.

    >>> times_table(3)
    array([[1, 2, 3],
           [2, 4, 6],
           [3, 6, 9]])
    >>> times_table(5)[4, 4]
    25
    """
    # make a 1-d array from value 1 up to the end of the n input range plus 1
    # the +1 is necessary due to stopping 1 value from the end
    rowOfRangeValues = np.arange(1, n +1)
    # now take this new range of values and reshape them from a row to a column
    # -1 = work out how many rows and 1 = one column
    reshapeRange = rowOfRangeValues .reshape(-1, 1)
    # multiply the rows of range values and the row reshaped as a column
    # shapes dont match but Numpy uses broadcasting stretches row and column across
    # then multiplies
    table = rowOfRangeValues  * reshapeRange
    # return the finished table
    return table


if __name__ == "__main__":
    times_table(3)

# ANSWER: (the QUESTION is at the top of this file)
# Numpy broadcasting lines up the shapes of the arrays from the right, so a 1-D array similar to c with a shape of (n,) is treated like a row with shape (1, n)
# Therefore, c needs to be added with columns so that c[j] will actually go into column j it then matches the columns of A(n, m) and numpy copies that row to all other n rows, so reshape is not needed.
# b then needs to be added along the rows so that b[i] will go into the row i, b already has shape of (n,) so numpy treats it as a row and lines it up with the m column which is incorrect so, b.reshape(-1,1)
# turns b into a column shaped (n, 1) which is then lined up with the rows of A and numpy copies it across all m columns. If b was not reshapen then when n does not equal m the shapes (n,m) and (n,)
# do not match and results in a numpy error. When n does equal m for example in the 4x4 example then it wouldnt throw an error but it would silemtly add b alongside the columns giving the wrong answer.
