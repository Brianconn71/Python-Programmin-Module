"""Drill. Counting the positions where two sequences disagree.

Run the tests:

    python -m doctest W07/E02_hamming.py

No output means every test passed.

Hamming distance is the first thing anyone tries, and the lecture spent Part 1
showing where it breaks. Write it, then write the version that copes with two
different lengths.
"""

from itertools import zip_longest
def hamming(a, b):
    """Count the positions where a and b differ, ignoring any extra tail.

    >>> hamming("ACGT", "ACGT")
    0
    >>> hamming("ACGTACGTAC", "ACGTTCGTAC")
    1
    >>> hamming("ACGTACGTAC", "CGTACGTACA")
    10
    """
    # Writing the hamming function as seen in lecture
    # zip(a,b) - basically will pair up the inputs added by user which are in same position
    # so zip("Brian", "Matt") will be ('B', 'M') etc etc for each letter, 
    # zip will stop at the end of the shorter string so any extra letters, values from the longer string get ignored,
    # hence the "ignore extra tail", x != y asks are thepairs different
    # which tehn will return a list of boolean values which will be true if values were same  and false if not
    # sum then sums the true values (1's) and returns the answer
    return sum([x != y for x , y in zip(a,b)])


def hamming_padded(a, b):
    """Count differing positions, counting each unmatched item as a difference.

    >>> hamming_padded("ACGT", "ACGT")
    0
    >>> hamming_padded("abc", "abcde")
    2
    >>> hamming_padded("", "abc")
    3
    >>> hamming_padded("abc", "")
    3
    """
    return  # YOUR CODE HERE


# `zip` stops at the shorter of the two, so `hamming` silently ignores
# everything past the end of it: hamming("abc", "abcde") is 0. That is why the
# lecture said Hamming cannot compare sequences of different lengths at all.
# `itertools.zip_longest` pads the shorter one with None instead, and None
# equals nothing, so every unmatched item counts as a difference.

if __name__ == "__main__":
    hamming("ACGTACGTAC", "ACGTTCGTAC")
