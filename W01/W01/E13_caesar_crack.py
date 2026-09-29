"""Extension. Letting the computer pick the right decoding.

Run the tests:

    python -m doctest W01/E13_caesar_crack.py

No output means every test passed.

QUESTION: crack fails on the short message below. Why? What would you
need in order to fix it? Write your answer in the comment at the bottom.
"""

# Given: the cipher from the lecture. You do not need to change it.
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def caesar(s, k):
    """Shift every letter of s forward by k places. Leave other characters alone."""
    # same function as what was in ex 12
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
    """Given: every possible decoding, as (k, plaintext) tuples."""
    # same function as in ex 12
    # except I used a list comprehension rather than a loop.
    # Comprehension fits the list, loop and append in the same line.
    return [(k, caesar(s, -k)) for k in range(26)]


def english_score(text):
    """Score how English-looking text is: count the commonest English letters.

    The six commonest letters in English are e, t, a, o, i, n. Count how
    many characters of text are one of those. Upper case counts too.

    >>> english_score("hello there")
    5
    >>> english_score("xyz")
    0
    >>> english_score("attack at dawn")
    8
    """
    # setting a set of common letters in the alphabet
    common = set("etaoin")
    # list comprehension to go through each input argument character and add 1 for each time a common letter is present.
    # .lower to account for and capitalized letter which may be used by the user.
    return sum(1 for c in text.lower() if c in common)


def crack(s):
    """Return the decoding of s that scores highest. No human required.

    >>> crack("wkh txlfn eurzq ira")
    'the quick brown fox'
    >>> crack("dvvk dv rk kyv sizuxv rk urne")
    'meet me at the bridge at dawn'
    >>> crack("ymj wfns ns xufns kfqqx rfnsqd ts ymj uqfns")
    'the rain in spain falls mainly on the plain'

    But it is only a guess, and on a short message it guesses wrong:

    >>> crack("khoor zruog")
    'ebiil tloia'
    """
    
    # list comprehension which returns the text with the maximum score, the key= is used to check what we should compare by
    return max((text for k, text in all_shifts(s)), key=english_score)


# ANSWER: (the QUESTION is at the top of this file)
#
# The message used is too short. Wrong shift used could contain more common letters than real answer.

# 2 ways to fix are below:
#   1. Score all 26 letters in alphabet by how common they are in english.
#   2. Ensure the words used are actual real words.
