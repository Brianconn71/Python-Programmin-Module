"""Extension. A three-button calculator, and an infinite graph.

Run the tests:

    python -m doctest W06/E05_calculator.py

No output means every test passed.

    A calculator has only three buttons. The first multiplies the current
    value by 3, the second adds 2, and the third subtracts 2. Starting from
    0, what is the least number of presses needed to reach 100?

    -- https://puzzling.stackexchange.com/questions/91090/

This is the river problem again with the labels changed. A state is a number,
a move is a button, and the shortest sequence of button presses is the
shortest path. Note what a state is *not*: it is not the buttons pressed so
far, just the number on the display. Two different histories that leave the
same number showing are the same state, and treating them as one is what
keeps the search small.

The graph here really is infinite -- there is no largest number -- so it could
never be built, and BFS explores only the part it needs.

QUESTION: `fewest_presses(100)` returns in a fraction of a second, but
`fewest_presses(10000)` will run until you stop it. Nothing is wrong with the
code. What is growing, and how fast? Write your answer in the comment at the
bottom.
"""

from E01_river import bfs


def calc_successors(n):
    """Yield the three numbers one button press away from `n`.

    >>> list(calc_successors(4))
    [12, 6, 2]
    >>> list(calc_successors(0))
    [0, 2, -2]
    """
    return  # YOUR CODE HERE


def presses(target):
    """The numbers on the display, one press at a time, starting from 0.

    >>> presses(10)
    [0, 2, 6, 8, 10]
    >>> presses(100)
    [0, 2, 4, 12, 36, 34, 102, 100]
    """
    return  # YOUR CODE HERE


def fewest_presses(target):
    """How few presses reach `target`, starting from 0?

    >>> fewest_presses(100)
    7
    >>> fewest_presses(10)
    4
    >>> fewest_presses(0)
    0
    """
    return  # YOUR CODE HERE


# ANSWER: (the QUESTION is at the top of this file)
