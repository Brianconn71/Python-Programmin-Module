"""Composition. How un-random is a sequence of keypresses? SOLUTION.

Run the tests:

    python -m doctest W02/E07_key_stats.py

No output means every test passed.

The oracle beats you because your typing has structure. These two functions
measure two kinds of structure directly, without any model at all.

QUESTION: for a genuinely random sequence, what would you expect switch_rate
to be? Write your answer in the comment at the bottom.
"""


def longest_run(history):
    """Return the length of the longest run of one repeated key.

    A run is a stretch of the same character. In "ffdff" the runs are
    "ff", "d", "ff", so the longest is 2.

    >>> longest_run("ffdff")
    2
    >>> longest_run("fffff")
    5
    >>> longest_run("fdfdfd")
    1
    >>> longest_run("f")
    1

    An empty history has no runs at all:

    >>> longest_run("")
    0
    """
    # if the input is empty then just return 0.
    if not history:
        return 0
    # initializing variables to start at 1 as we have dealt with empyt inputs with if statement above so anything else starts as a 1 at a minimum.
    count = 1
    highest = 1
    # use slicing to get the very first character in the input
    first_letter = history[0]
    # start the for loop from the second character in the input using slicing [1:]
    # keep looping to the end as no end value added.
    for letter in history[1:]:
        # in this iteration does the value equeal the first character which we initialized above as the first_letter?
        if letter == first_letter:
            # count variable gets updated to add 1 as key is repeated
            count += 1
            # highest variable now checks if the count variable is greater than the count
            # if count is bigger then update highest variable.
            highest = max(highest, count)
        else:
            # if values arent equal then count stays the same
            count = 1
        # now before, looping again we change the first_letter variable to equal the value of the value in this iteration and loop again with a new first_letter variable value equalling the previous character we looped through.
        first_letter = letter
    # once finished we return the maximum count value stored in the highest variable to symbolise longest run of same values.
    return highest


def switch_rate(history):
    """Return the fraction of keypresses that differed from the one before.

    Count the places where the key changed, and divide by the number of
    places where it could have changed, which is one less than the length.

    >>> switch_rate("fdfdfd")     # changes every time
    1.0
    >>> switch_rate("ffffff")     # never changes
    0.0
    >>> switch_rate("ffdd")       # one change out of three chances
    0.3333333333333333
    >>> round(switch_rate("fdfdff"), 2)
    0.8

    A sequence with no pairs in it has no chances to change, so there is
    nothing to average and we say 0.0 rather than dividing by zero:

    >>> switch_rate("f")
    0.0
    >>> switch_rate("")
    0.0
    """
    # if statement to deal with a case where there are no pairs and has no reason to divide.
    # divide by zero would give an error.
    if len(history) <=1:
        return 0.0
    
    #gets the first value from our input argument to the function.
    previous_letter = history[0]
    # initialize count variable to start at 0
    count = 0
    
    # looping through the input from the second value onwards.
    for value in history[1:]:
        if value != previous_letter:
            count += 1
        previous_letter = value

    answer = count / (len(history) - 1)


    return  float(answer)


# ANSWER: (the QUESTION is at the top of this file)
