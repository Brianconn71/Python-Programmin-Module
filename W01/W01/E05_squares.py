"""Drill. Building a list with append.

Run the tests:

    python -m doctest W01/E05_squares.py

No output means every test passed.
"""


def squares(n):
    """Return a list of the squares of 1 up to and including n.

    >>> squares(4)
    [1, 4, 9, 16]
    >>> squares(1)
    [1]
    >>> squares(0)
    []
    """
    list = []
    for x in range(1, n+1):
        t = x ** 2
        list.append(t)
    return list

"""def squares(n):
    Return a list of the squares of 1 up to and including n.

    squares(4)
    [1, 4, 9, 16]
    squares(1)
    [1]
    squares(0)
    []
    
    return [x ** 2 for x in range(1, n + 1)]

A couple of things worth pointing out about the original:

list as a variable name shadows the built-in list type. It works fine here since you don't need the built-in inside this function, but it's a habit worth breaking — if you ever needed to call list(something) later in the same function, it would break.
The t variable was just a temporary holding spot for x ** 2 before appending — not needed once you use a comprehension, since the expression goes directly where the value would go.
"""