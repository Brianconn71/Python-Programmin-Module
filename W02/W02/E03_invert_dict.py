"""Drill. A dict comprehension.

Run the tests:

    python -m doctest W02/E03_invert_dict.py

No output means every test passed.

QUESTION: the last doctest below loses a pair. Why? Write your answer in
the comment at the bottom.
"""


def invert_dict(d):
    """Return a new dict with every key-value pair the other way round.

    Use a dict comprehension: {new_key: new_value for k, v in d.items()}.

    >>> invert_dict({"a": 1, "dog": 3, "giraffe": 7})
    {1: 'a', 3: 'dog', 7: 'giraffe'}
    >>> invert_dict({})
    {}

    Inverting twice gets you back where you started:

    >>> invert_dict(invert_dict({"a": 1}))
    {'a': 1}

    But not always:

    >>> invert_dict({"a": 1, "b": 1})
    {1: 'b'}
    """
    # dict comprtehension
    # essentially it loops through the key value pairs in the dictionary and creates a new dictionary with original value as key and vice versa.
    return {v:k for k, v in d.items()}


# ANSWER:
# Doctest loses a pair as Key values need to be unique
# {"a": 1, "b": 1} becomes inverted we get two separate keys with the same value which is not allowed in dictionaries.
# So, essentially, 1: "b" overwrites 1:"a" and "a" becomes lost
