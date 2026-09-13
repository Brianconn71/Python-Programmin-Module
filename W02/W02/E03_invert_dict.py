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
    return  # YOUR CODE HERE


# ANSWER: (the QUESTION is at the top of this file)
