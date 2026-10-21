"""Drill. Fibonacci from the bottom up.

Run the tests:

    python -m doctest W07/E03_fib_table.py

No output means every test passed.

The lecture's `fib_slow` is exponential because it asks the same questions over
and over. Fill a table instead, smallest first, so each answer is computed
once. Then notice how little of that table you actually needed.
"""
def fib_table(n):
    """Return the nth Fibonacci number, building a list from the bottom up.

    >>> [fib_table(i) for i in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> fib_table(35)
    9227465
    """
    # fibonacci sequence starts with 0 & 1 and builds up
    # start the fibonacci table with the first two fibonacci numbers.
    fibonacci = [0, 1]

    # Now start the loop from two and go to the end of the input
    # we need to add + 1 to input or it will stop one place short
    for i in range(2, n +1):
        # now we append the add the two previous numbers to get the next value for the list and add it to the end using append
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    # return the final value in the list fibonacci which answers the question
    # Return the nth Fibonacci number
    return  fibonacci[n]


def fib_pair(n):
    """The same answer, keeping only the two values we still need.

    >>> [fib_pair(i) for i in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    >>> fib_pair(35)
    9227465
    >>> all(fib_pair(i) == fib_table(i) for i in range(50))
    True
    """
    # setup first two numbers of fibonacci sequesnce as 0 & 1
    a, b = 0, 1
    # I won't be using the loop variable inside the loop so using _ 
    # I need Loop to loop n times withoput using the value within the loop
    for _ in range(n):
        # for every loop move a and b numbers forward
        # a becomes the new value of old b 
        # b becomes the value of old a + old b
        # right hand side of the variable is calculate before assigning the new values
        a, b = b, a + b
    # Once the loop has finished return value a which will hold the nth fibonacci number
    return a


# `fib_table` holds n numbers to return one. `fib_pair` holds two. This is the
# same saving we make for edit distance in E05, one dimension down: look at the
# recurrence, see how far back it actually reaches, and keep only that much.

if __name__ == "__main__":
    fib_pair(35)