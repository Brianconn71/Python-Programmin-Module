"""Drill. The same walk, collecting instead of adding.

Run the tests:

    python -m doctest W03/E04_flatten.py

No output means every test passed.
"""


def flatten(items):
    """Return a flat list of every number in items, in the order they appear.

    Same two cases as nested_sum. The only difference is what you do with
    the answer from below: append adds one item, extend adds all the items
    of another list.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> flatten([1, [2, 3], [4, [5]]])
    [1, 2, 3, 4, 5]
    >>> flatten([])
    []
    >>> flatten([[], [[]]])
    []
    >>> flatten([[[[7]]]])
    [7]
    """
    # new list initialized
    out = []

    # loop through the items inside list argument
    for item in items:
        # if the item is a list
        if isinstance(item, list):
            # then take this list and run it back through the function again.
            out += flatten(item)
        else:
            # if its not a list, then we are adding the item to our newly created list
            out.append(item)
    # then we return the list.
    return out

def flatten_extend(items):
    """Return a flat list of every number in items, in the order they appear.

    Same two cases as nested_sum. The only difference is what you do with
    the answer from below: append adds one item, extend adds all the items
    of another list.

    >>> flatten_extend([1, 2, 3])
    [1, 2, 3]
    >>> flatten_extend([1, [2, 3], [4, [5]]])
    [1, 2, 3, 4, 5]
    >>> flatten_extend([])
    []
    >>> flatten_extend([[], [[]]])
    []
    >>> flatten_extend([[[[7]]]])
    [7]
    """
    # added in a new function to deal with extend method, same as above except
    # we use recursion to send the list through the function while adding the whole list to the outpur.
    out = []

    for item in items:
        if isinstance(item, list):
            # recurse first and then extend the flattened result.
            out.extend(flatten_extend(item))
        else:
            out.append(item)

    return out
