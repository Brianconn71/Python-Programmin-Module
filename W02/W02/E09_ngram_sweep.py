"""Extension. Which value of n is best -- for you? SOLUTION.

Run the tests:

    python -m doctest W02/E09_ngram_sweep.py

No output means every test passed.

Playing a game takes minutes. Replaying a saved one takes milliseconds, so we
can try every value of n on the same keypresses and compare them fairly. This
is what "run an experiment" means, and Week 7 does it properly.

QUESTION: run the sweep on your own history and write the numbers into the
comment at the bottom. Which n was best, and why do the big ones fall away?
"""

from collections import Counter
from pathlib import Path

DATA = Path(__file__).parent / "data"

# Given: the model from the lecture, with two changes.
#
#   1. The context length k is an argument, not a global, so one run of the
#      program can try several values.
#   2. A tie goes to "f" rather than being broken at random. The real oracle
#      guesses, which is right for a game but wrong for an experiment: we need
#      the same input to give the same number every time we run it.
def predict(counts, history, k):
    context = history[-k:]
    if counts[context + "d"] > counts[context + "f"]:
        return "d"
    return "f"


def update(counts, history, key, k):
    counts[history[-k:] + key] += 1


def accuracy(history, k):
    """Replay `history` past the model and return the fraction it got right.

    Exactly the lecture's loop: predict, score, learn, move on. The model
    starts empty and learns as it goes, so it is being tested only on
    keypresses it has not seen -- which is the honest way to do it.

    An empty model predicts "f", so a history of all f's is a clean sweep:

    >>> accuracy("ffffffffff", 1)
    1.0

    Alternating is learned after one mistake at the start:

    >>> accuracy("fdfdfdfdfd", 1)
    0.9

    A longer context has more to learn, so it takes longer to get going:

    >>> accuracy("fdfdfdfdfd", 2)
    0.8
    >>> accuracy("ffddffddff", 2)
    0.8
    >>> accuracy("ffddffddff", 4)
    0.6

    Nothing to predict, nothing to score:

    >>> accuracy("", 3)
    0.0
    """
    # initialize the counts variable which will be used to count each pattern was followed by f or d
    counts = Counter()
    # initializing below variables to start at nothing before being updated inside the loop
    seen = ""
    correct = 0
    total = 0

    # loops through the values input into function parameter
    for value in history:
        # For guess, call the predict function with the count of the patterns.
        # k which is user input to be the number of keys.
        # Seen which is the number of keys we have seen concatenated.
        # Value from this function is then stored in guess variable. 
        guess = predict(counts, seen, k)
        # if the guess value is the same as the value we are currently iterating with
        if guess == value:
            # then we are correct so correct variable needs to be update plus 1
            correct += 1
        # where model is learning.
        # call update function with counts - the patterns
        # seen which the string of values we have now seen concatenated together
        # and the value which is the current value we are iterating with.
        update(counts, seen, value, k)
        # Seen variable now concatenates the value we are iterating with.
        # seen now should grow with key presses
        seen += value
        # the total value gets updated plus 1
        # means we have made another prediction and added to total predictions
        total += 1
    # If the loop never runs then total will be 0
    if total == 0:
        # as a result we return 0.0 to overcome divide by zero errors.
        return 0.0
    # return the divison of correct by the total value which should give us the predictions that were right as a decimal / float value.
    return correct / total


def sweep(history, ks=range(1, 9)):
    """Return {k: accuracy} for each k, so the values can be compared.

    >>> sweep("fdfdfdfdfd", [1, 2, 3])
    {1: 0.9, 2: 0.8, 3: 0.8}
    """
    # dictinary comprehension - runs the accuracy function with history agument by the user
    # returns for us a dictionary of the accuracy of the predictions with user input history and list of the number of key values to remember.
    return {k: accuracy(history, k) for k in ks}


if __name__ == "__main__":
    # Replay the sample session that ships with the exercise. Swap in your own
    # by using E08's load_histories("your_id") instead.
    history = (DATA / "history_sample.txt").read_text().strip()
    print(f"{len(history)} keypresses")
    for k, score in sweep(history).items():
        print(f"  n = {k + 1:2d}  (k = {k})   {score:.1%}")


# ANSWER: (the QUESTION is at the top of this file)
# ran python3 E09_ngram_sweep.py and got below results
# 600 keypresses
#  n =  2  (k = 1)   87.5%
#  n =  3  (k = 2)   87.2%
#  n =  4  (k = 3)   86.8%
#  n =  5  (k = 4)   86.3%
#  n =  6  (k = 5)   86.0%
#  n =  7  (k = 6)   85.3%
#  n =  8  (k = 7)   84.2%
#  n =  9  (k = 8)   83.0%

# n of value 2 received the best score 
# With longer n values the computer could capture more patterns but there may not be enough to learn from it.
# small n is efficient, big n needs more data to sufficiently learn from it.
