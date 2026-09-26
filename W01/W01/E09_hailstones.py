"""Composition. Hailstone sequences.

Run the tests:

    python -m doctest W01/E09_hailstones.py

No output means every test passed.
"""


def hailstones(n):
    """Return the hailstone sequence starting at n and ending at 1.

    If n is even, the next number is n/2. If n is odd, it is 3n+1.

    >>> hailstones(1)
    [1]
    >>> hailstones(10)
    [10, 5, 16, 8, 4, 2, 1]
    >>> hailstones(7)[:6]
    [7, 22, 11, 34, 17, 52]
    >>> len(hailstones(27))
    112
    """
    # take the input and transform to a list
    list = [n]
    # if input is 1 dont go into loop and just return the 1.
    while n != 1:
        # modulo of the input divided by 2, if not 0 its odd
        if n % 2 != 0:
            # so if odd we times by three
            n = (3 * n) + 1
        else:
            # Otherwither wise by 2
            n = n //2
        # then append, new number to the list
        list.append(n)
    # return the list.
    return list


def longest_hailstone(limit):
    """Return (n, length) for the longest hailstone sequence with n < limit.

    >>> longest_hailstone(10)
    (9, 20)
    >>> longest_hailstone(100)
    (97, 119)
    >>> longest_hailstone(1000)
    (871, 179)
    """
    # initialize best number of hailstones as 1, best cant be 0
    best_number = 1
    # initalize the best length of the sequence as 1
    best_length = len(hailstones(1))

    # loop through inout and start with best number as two otherwise dont enter the loop.
    for value in range(2, limit):
        # cureent best lenght which is the value inside the input used to get the list in hailstones function
        length = len(hailstones(value))
        # if current length is better than the current best
        if length > best_length:
            # we initialize the variables as the value from the input and the length of the list we gewt basck from hailstones.
            best_number = value
            best_length = length
    # return the best number with the best sequence as a tuple
    return  best_number, best_length
