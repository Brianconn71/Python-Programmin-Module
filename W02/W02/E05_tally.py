"""Drill. Counting, by hand and with Counter.

Run the tests:

    python -m doctest W02/E05_tally.py

No output means every test passed.
"""

from collections import Counter


def tally(xs):
    """Return a plain dict mapping each item of xs to how often it appears.

    Do it by hand: start with an empty dict and walk the list once.

    >>> tally(["red", "blue", "red"])
    {'red': 2, 'blue': 1}
    >>> tally([])
    {}
    >>> tally("banana")
    {'b': 1, 'a': 3, 'n': 2}
    """
    # new dict intialized
    new_dict = {}
    # loop through the values in the input list.
    for value in xs:
        # if the value is already in the new dictionary
        if value in new_dict:
            # then we add 1 to the running total/counter.
            new_dict[value] += 1
        else:
            # if its not in the dictionary then we initalize a new key pair in the dictionary
            new_dict[value] = 1
    # then return the newly created dictionary.
    return new_dict


def tally_counter(xs):
    """The same thing, in one line, using Counter (already imported above)

    A Counter prints its items most-common-first, which is why the output
    below is in a different order from tally's.

    >>> tally_counter(["red", "blue", "red"])
    Counter({'red': 2, 'blue': 1})
    >>> tally_counter("banana")
    Counter({'a': 3, 'n': 2, 'b': 1})

    A Counter is a dict, so it is indexed like one -- except that a missing
    key gives 0 rather than a KeyError:

    >>> tally_counter("banana")["a"]
    3
    >>> tally_counter("banana")["z"]
    0
    """
    # this function is essentially the same as whats above but uses Pythons built in Counter 
    # Counter loops over the input list and keeps counts of each item it sees in it.
    return Counter(xs)
