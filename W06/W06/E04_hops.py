"""Composition. How far is everywhere, in moves? SOLUTION.

Run the tests:

    python -m doctest W06/E04_hops.py

No output means every test passed.

One BFS answers "how far is the goal?" for every goal at once, because a
state is first reached along a shortest path to it. Keep the distance instead
of the predecessor and you get the whole table for the price of one search.

QUESTION: `hops_from` records a distance for a state the first time it sees
that state, and never changes it afterwards. Why is that safe here, and what
would go wrong on `ROADS` if the numbers we wanted were minutes rather than
roads? Write your answer in the comment at the bottom.
"""

from collections import deque

from E01_river import ROADS, START, successors


def hops_from(successors, start):
    """How many moves each reachable state is from `start`, as a dict.

    `start` itself is 0. Everything else is one more than the state it was
    first reached from.

    >>> hops_from(successors, START)["RRRR"]
    7
    >>> hops_from(successors, START)["RLRL"]
    1

    Four roads from Galway to Clifden, whichever way you go:

    >>> hops_from(lambda town: ROADS[town], "Galway")["Clifden"]
    4
    >>> hops_from(lambda n: {"a": "b", "b": "a"}[n], "a") == {"a": 0, "b": 1}
    True
    """
    # Function is incredibly similar to bfs method in E01_river.py
    # This creates a Queue of the places not explored. so it will start with what we pass 
    # to it a an input argument in place of start variable. deque is similar to a list but faster
    frontier = deque([start])
    # We initalize a start state dictionary with the initial input argument 'start' as a key and an initial value of 0
    # At the end of the function this dictionary is what will be returned to the user.
    hopsAway = {start: 0}

    # Loop through the frontier queue while it remains with values
    while frontier:
        # First in first out, popleft will take the oldest state off front of queue
        # essentially, all states 1 move away get prioritised over those 2 moves away
        state = frontier.popleft()
        # successors gives the states one move away
        for nxt in successors(state):
            # if we have not yet visited this state - it wont be in hopsAway.
            if nxt not in hopsAway:
                # Given the nxt town wont have been visited we will add it to the dictionary
                # The value of this key will store how many moves/hops away from the start this town or state will be
                # so, 'Clifden' : 1, 'Recess': 2 etc,
                hopsAway[nxt] = hopsAway[state] + 1
                # and finally put it back on the queue
                frontier.append(nxt)
    # once the queue is empty we have then visited everywhere we need to so we now return this dictionary to the user.
    return hopsAway


def farthest_hops(successors, start):
    """The distance to the state that is hardest to reach from `start`.

    >>> farthest_hops(successors, START)
    7
    >>> farthest_hops(lambda town: ROADS[town], "Galway")
    4
    """
    return  max(hops_from(successors, start).values())


if __name__ == "__main__":
    hops_from(successors, START)["RRRR"]
    farthest_hops(successors, START)

# ANSWER: (the QUESTION is at the top of this file)
