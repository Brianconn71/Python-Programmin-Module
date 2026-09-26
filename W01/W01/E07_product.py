"""Drill. Python has sum() built in, but not product().

Run the tests:

    python -m doctest W01/E07_product.py

No output means every test passed.
"""


def product(L):
    """Return the product of the numbers in L.

    The sum of an empty list is 0, but the product of an empty list is 1.

    >>> product([1, 1, 1])
    1
    >>> product([1, 2, 3])
    6
    >>> product([])
    1
    >>> product([2, 3, 4])
    24
    """
    # initialize the product as 1 as the product of an empty input will be 1
    product = 1

    # loop through the input
    for value in L:
        # product is previous value * new value so new loop value * the product we initalized which will then change to new value once loop moves through to next stage
        product *= value

    # return our product value.
    return product
