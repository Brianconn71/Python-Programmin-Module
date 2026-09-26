"""Composition. Rotation, in one line, with slicing.

Run the tests:

    python -m doctest W01/E11_rotate.py

No output means every test passed.
"""


def rotate(s, k):
    """Move the first k items of s to the end.

    This is the trick that made the cipher easy in the lecture. It works on
    a list as well as a string. If k is bigger than s, wrap around.

    >>> rotate("abcdef", 2)
    'cdefab'
    >>> rotate("abcdef", 0)
    'abcdef'
    >>> rotate([1, 2, 3, 4], 1)
    [2, 3, 4, 1]
    >>> rotate("abc", 3)
    'abc'
    >>> rotate("abc", 4)
    'bca'
    >>> rotate("", 2)
    ''
    """
    # if the input is blank then return what was input i.e in this case an empty string is returned.
    if not s:
        return s
    
    # Modulo of the lenght of the input divided by the cipher number input
    # eg. if k = 7 and len(s) = 5 then 7% 5 = 2
    k = k % len(s)
    # so now we return a new input to the user which splits based on the index provided by k above
    return s[k:] + s[:k]
