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
    shifted = ALPHABET[k % 26:] + ALPHABET[:k % 26]
    out = []
    for c in s:
        if c in ALPHABET:
            out.append(shifted[ALPHABET.index(c)])
        else:
            out.append(c)
    return "".join(out)


def all_shifts(s):
    """Given: every possible decoding, as (k, plaintext) tuples."""
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
    common = set("etaoin")
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
    
    return max((text for k, text in all_shifts(s)), key=english_score)


# ANSWER: (the QUESTION is at the top of this file)
#
# "khoor zruog" is only 10 letters, so counting occurrences of e/t/a/o/i/n
# is too noisy to be reliable: on such a short message, some wrong shift
# can rack up as many (or more) of those six letters as the true plaintext
# purely by chance, so english_score picks the wrong winner.
#
# To fix it, the scoring function needs more signal than six letter counts
# on a handful of characters. Two options:
#   1. Score against the full English letter-frequency distribution (all
#      26 letters, weighted by how common each is) instead of a crude
#      count of six letters — still noisy on short text, but less so.
#   2. Check candidate words against a dictionary of real English words.
#      "hello world" are real words and "ebiil tloia" are not, so this
#      would decisively pick the right decoding even for short messages,
#      because it doesn't rely on statistics at all.
