"""Composition. Deciding whether two arrays can be broadcast together.

Run the tests:

    python -m doctest W08/E05_broadcastable.py

No output means every test passed.

Numpy's rule is short. Line the two shapes up at the *right* hand end, and
pad the shorter one with 1s on the left. Two axes are compatible if they are
equal, or if either of them is 1. If every pair is compatible the arrays can
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
    r = X.shape
    u = Y.shape
    g = X[::-1]
    m = Y[::-1]
    for c,v in zip(g,m):
        if g != m or g != 1 or m !=1:
            return False
    return True

if __name__ == "__main__":
    is_broadcastable(np.zeros((3, 5)), np.zeros(3))
