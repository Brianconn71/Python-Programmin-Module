"""Extension. The same idea, for cube roots.

Run the tests:

    python -m doctest W01/E14_newton_cbrt.py

No output means every test passed.
"""

# Given: the iterate function from the lecture, with one addition -- a limit on
# the number of steps, so that a wrong transform gives up instead of hanging.
# You do not need to change it.
def iterate(x, transform, done, max_steps=10000):
    """Apply transform to x over and over, until done(x) is true."""
    for _ in range(max_steps):
        if done(x):
            return x
        x = transform(x)
    raise RuntimeError("iterate: gave up after too many steps")


def newton_cbrt(x, tol=1e-10):
    """Return the cube root of x.

    Use iterate. The transform replaces the guess g with (2*g + x/(g*g)) / 3.
    Stop when g cubed is within tol of x.

    Unlike square roots, cube roots of negative numbers are perfectly well
    defined, so this function should not raise.

    >>> round(newton_cbrt(27), 6)
    3.0
    >>> round(newton_cbrt(8), 6)
    2.0
    >>> round(newton_cbrt(2), 6)
    1.259921
    >>> round(newton_cbrt(-8), 6)
    -2.0
    """
    # below are two helper functions transform and done

    # transform takes the current guess and tries to return a better guess
    def transform(g):
        # 2 times the input guess plus the input argument x divided by
        # the guess times itself and then divide it all by three
        return (2 * g + x / (g * g)) / 3

    # done takes the guess and checks if its good enough to reurn True and stop.
    def done(g):
        # cube the guess minus the input argument is how close from guess we are the abs turns to positive number
        # < tol is used to check the tolerance of the guess, is it small enough?
        return abs(g ** 3 - x) < tol

    # Passes both functions to iterate which uses the for loop to run until a sufficient answer is obtained.
    return iterate(1.0, transform, done)
