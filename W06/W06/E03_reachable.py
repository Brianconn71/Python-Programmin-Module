"""Composition. Search with no goal: where could we possibly get to? SOLUTION.

Run the tests:

    python -m doctest W06/E03_reachable.py

No output means every test passed.

`bfs` stops as soon as it finds the goal. Take the goal away and let it run to
exhaustion, and what you have explored is the whole connected part of the
graph. That is how you find out how big a state space really is.
"""

from collections import deque

from E01_river import ROADS, START, successors


def reachable(successors, start):
    """Every state reachable from `start`, as a set. `start` itself counts.

    Breadth-first search with the goal test removed: keep a frontier and a
    visited set, and stop when the frontier runs dry.

    The river has sixteen states on paper and ten that are safe, and every
    safe one can actually be reached:

    >>> len(reachable(successors, START))
    10

    A dict is not a successor function, but a `lambda` turns it into one:

    >>> len(reachable(lambda town: ROADS[town], "Galway"))
    12
    >>> sorted(reachable(lambda n: {"a": "b", "b": "a", "c": ""}[n], "c"))
    ['c']
    """
    # This creates a Queue of the places not explored. so it will start with what we pass 
    # to it a an input argument in place of start variable. deque is similar to a list but faster
    frontier = deque([start])
    # Creates a set of every state that has been seen. starts off with the stating point which
    # is the start argument sent by the user as this will have been visited and should not be added again,
    # Sets take in unique values with no duplictes so if we later travel through clifden twice it 
    # will only get added once.
    visited = set([start])

    # keep looping while queue is not empty
    while frontier:
        # First in first out, popleft will take the oldest state off front of queue
        # essentially, all states 1 move away get prioritised over those 2 moves away
        state = frontier.popleft()
        # successors is a generator function, loops over the value which is one move away from this state.
        for nxt in successors(state):
            # if we have not yet visited this state - it wont be in visited.
            if nxt not in visited:
                # then we will add this syaye/neighbour to the viited set
                visited.add(nxt)
                # and finally put it back on the queue
                frontier.append(nxt)
    # once the queue is empty we have then visited everywhere we need to so we now return this set to the user.
    return visited


def connected(successors, a, b):
    """Is there any route at all from `a` to `b`?

    >>> connected(successors, "LLLL", "RRRR")
    True

    "LLRR" is the wolf and the goat left alone together. It is a state you can
    write down, and there is no way to reach it:

    >>> connected(successors, "LLLL", "LLRR")
    False
    """
    return  # YOUR CODE HERE
