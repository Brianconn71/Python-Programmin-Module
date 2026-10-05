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
            # this will then rerun nested_sum with the item iteration as an argument.
            count += nested_sum(item)
        else:
            # if item is now no longer a list we are expecting a number here so 
            # count gets updated to be the running count plus the new value item.
            # example 2 + 3 = 5
            count += item
    
    # now return the total which in this case is the variable count and it will be the answer to the question.
    return  count

