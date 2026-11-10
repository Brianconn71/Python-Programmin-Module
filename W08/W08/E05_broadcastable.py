"""Composition. Deciding whether two arrays can be broadcast together.

Run the tests:

    python -m doctest W08/E05_broadcastable.py

No output means every test passed.

Numpy's rule is short. Line the two shapes up at the *right* hand end, and
pad the shorter one with 1s on the left. Two axes are compatible if they are equal, or if either of them is 1. If every pair is compatible the arrays can
be broadcast together; if any pair is not, Numpy raises an error.

So (4, 1) and (1, 4) are fine, and so are (3, 5) and (5,), but (3, 5) and
(3,) are not: lined up at the right, 5 and 3 disagree and neither is 1.

Write the rule out yourself. You only need the shapes, never the values.
"""
import numpy as np
# Needed to add this line as was having issues with numpy versions
# I had numpy 2.5 installed, newer numpy does not need np.int64(1)
np.set_printoptions(legacy="1.25")


def is_broadcastable(X, Y):
    """Can X and Y be added together, using Numpy's broadcasting rules?

    >>> is_broadcastable(np.zeros((4, 1)), np.zeros((1, 4)))
    True
    >>> is_broadcastable(np.zeros((3, 5)), np.zeros(5))
    True
    >>> is_broadcastable(np.zeros((3, 5)), np.zeros(3))
    False
    >>> is_broadcastable(np.zeros((2, 3, 4)), np.zeros((3, 1)))
    True
    >>> is_broadcastable(np.zeros((2, 3)), np.zeros((4, 3)))
    False
    """
    # Below gets the shape of the arrays which will be compared in the loop
    # It will turn x_shape and y_shape into tuples with the shapes of X and Y as values
    x_shape = X.shape
    y_shape = Y.shape

    # Here, we reverse the tuples of shape values because using zip to loop over two loops at once lines them up from the left hand side
    # do we need to loop through them from the right so reversing the tuples helps with zip and pairing from the right hand side.
    x_reverersed = x_shape[::-1]
    y_reversed = y_shape[::-1]

    # Loop through both tuples at once and compare values against each other.
    for x_value,y_value in zip(x_reverersed,y_reversed):
        # Two axes are compatible if they are equal, or if either of them is 1. If every pair is compatible the arrays can be broadcast together
        # so, if the x_value in the loop does not equal the y_value, if x_value is not 1 and if y_value is not 1 then they are not compatible and return
        # false
        if x_value != y_value and x_value != 1 and y_value !=1:
            return False
    # otherwise, thhe two arrays are compatible and can be added together so return True
    return True

if __name__ == "__main__":
    is_broadcastable(np.zeros((3, 5)), np.zeros(3))
