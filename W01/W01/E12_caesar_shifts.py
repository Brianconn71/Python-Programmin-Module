"""Extension. Breaking the cipher by brute force.

Run the tests:

    python -m doctest W01/E12_caesar_shifts.py

No output means every test passed.
"""

# Given: the cipher from the lecture. You do not need to change it.
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def caesar(s, k):
    """Shift every letter of s forward by k places. Leave other characters alone."""
    # builds the alphabet rotated by whatever k is
    # k % 26 is what keeps the shift between 0 and 25
    shifted = ALPHABET[k % 26:] + ALPHABET[:k % 26]
    # initialize an empty list
    out = []
    # for each individual letter 
    for letter in s:
        # if the letter is in our already initialized alphabet string
        if letter in ALPHABET:
            # then append the letter in the index of shifted o the new list so if k = 4 a = e
            out.append(shifted[ALPHABET.index(letter)])
        else:
            # if its not in the alphabet then just add it to the new list
            out.append(letter)
    # then return the list as one string
    return "".join(out)


def all_shifts(s):
    """Return every possible decoding of s, as a list of (k, plaintext) tuples.

    Entry k says: if the message was encoded with a shift of k, it reads
    like this. There are 26 possible shifts.

    >>> shifts = all_shifts("khoor")
    >>> len(shifts)
    26
    >>> shifts[0]
    (0, 'khoor')
    >>> shifts[3]
    (3, 'hello')
    >>> shifts[3][1]
    'hello'
    """
    # intialize a new list
    l = []
    # loop over the value in the range 0-25
    for i in range(0, 26):
        # CAll the caesar function above with the index number in the loop iterations and shift the message backwards
        decoded = caesar(s, -i)
        # append the decoded letter to the new list and index value to the list as a tuple
        l.append((i , decoded))
    # return the decoded letter / message
    return  l
