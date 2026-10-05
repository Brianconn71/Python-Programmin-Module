"""Drill. Recursion, on the simplest possible nested data.

Run the tests:

    python -m doctest W03/E03_nested_sum.py

No output means every test passed.
"""


def nested_sum(items):
    """Total every number in items, however deeply nested the lists are.

    Two cases, as always. An item is either a list, which we have to look
    inside, or a number, which we can just add.

    isinstance(x, list) is how you ask whether x is a list.

    >>> nested_sum([1, 2, 3])
    6
    >>> nested_sum([1, [2, 3], [4, [5]]])
    15
    >>> nested_sum([])
    0
    >>> nested_sum([[], [[]]])
    0
    >>> nested_sum([[[[7]]]])
    7
    """
    # initialize empty count variable which will hold a running total of the sum.
    count = 0

    # Loop through the items in the input argument. 
    for item in items:
        # using python built in method to ask if the iteration is a list or not.
        if isinstance(item, list):
            # if it is a list then we run the function again on the list argument.
            # this will then 
            count += nested_sum(item)
        else:
            count += item
    
    return  count

if __name__ == "__main__":
    nested_sum([1, [2, 3], [4, [5]]])
