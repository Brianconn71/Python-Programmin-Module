"""Composition. Using a classifier: make one, fit it, predict, score.

Run the tests:

    python -m doctest W09/E08_estimator.py

No output means every test passed.

The classifier is the one from the lecture, imported rather than copied.
Every scikit-learn estimator has the same four moves, and once you know them
on one you know them on all of them:

    model = KNN(k=3)        make one, with its settings
    model.fit(X, y)         learn from rows X with labels y
    model.predict(X)        one label per row of X
    model.score(X, y)       the fraction it gets right

X is a table of numbers: one row per thing, one column per measurement.
y is one label per row. Here both are tiny and hand-written, so you can see
by eye what the answers should be.
"""

import numpy as np

from E01_penguins import KNN

# Given: four birds, each with one measurement, and what they are. The two
# light ones are storks, the two heavy ones are swans.
X = np.array([[3.0], [3.5], [10.0], [11.0]])
Y = np.array(["stork", "stork", "swan", "swan"])


def train(X, y, k):
    """Return a KNN with k neighbours, already fitted to X and y.

    fit returns the model itself, so this is one line.

    >>> model = train(X, Y, 1)
    >>> model.k
    1
    >>> hasattr(model, "X_")      # fitted, so it has remembered its data
    True
    """
    #setting up a knn classifier and setting it with k as the k value entered by user
    # this k is what is used to guess/predict based on neighbour proximity
    # k = 5 means base this prediction on the 5 nearest neighbouring values to the one we are predicting
    model = KNN(k=k)
    # then we are returning a KNN classifier already set to k neighbours and fitted based
    # on the input X rows and y labels from the user
    # fit returns the actual model which can be used for predicting and scoring later
    return model.fit(X, y)



def label_for(model, row):
    """What does the model call a single bird? Return a plain string.

    predict expects a *table* of rows, not one row, so a single bird has to
    be wrapped in a list before it goes in -- and the one answer has to be
    taken back out of the array that comes back.

    >>> model = train(X, Y, 1)
    >>> label_for(model, [3.2])
    'stork'
    >>> label_for(model, [10.5])
    'swan'

    With three neighbours voting, a bird in the middle is outvoted by
    whichever side is closer to it:

    >>> label_for(train(X, Y, 3), [6.0])
    'stork'
    """
    # row is coming into the function as a single row of values
    # predict expects a table/grid of lists of rows so, we take the input row r and make it a 
    # nested row which can then be past to predict method to make a prediction for the row input value
    nestedRow = [row]
    # we now use predict functionality to make a prediction on the input row label value
    # this returns an array so to get the label value we add [0] to return first value from array
    # we wrap it in a str() which ensures we get a plain string return value
    return str(model.predict(nestedRow)[0])


def accuracy(model, X, y):
    """The fraction of X that the model labels correctly, as a plain float.

    >>> model = train(X, Y, 1)
    >>> accuracy(model, X, Y)            # it has seen these before
    1.0

    Two birds it has not seen, one of which it gets wrong: 6.5 is nearer to
    3.5 than to 10.0, so it is called a stork.

    >>> accuracy(model, np.array([[3.1], [6.5]]), np.array(["stork", "swan"]))
    0.5
    """
    # now we use the score method which gets the fraction of X that gets correctly labelled.
    # We are asked to return it as a plain float so use python builtin float method to ensure compatibility
    return float(model.score(X, y))


if __name__ == "__main__":
    model = train(X, Y, 1)
    label_for(model, [3.2])
    accuracy(model, X, Y)

# Write it once yourself, then use the built-in for the rest of your life:
# accuracy is model.score with a float() round it. Every scikit-learn
# classifier has score, so you never have to write the counting loop.
