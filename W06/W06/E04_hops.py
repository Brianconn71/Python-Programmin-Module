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
    # One line composition
    # using the hops_fromfunction to return a dictionary of how far away all the states are from the original state added as an input 
    # argument to hops_from function.
    # then, we need to get the state which is hardest to reach from the start which will have the highest integer value next to the key as a key/value pair
    # Each new states value is one more than the state it has been reached from so the most difficult destination to reach should always have the hisghest value.
    return  max(hops_from(successors, start).values())


# ANSWER: (the QUESTION is at the top of this file)
# In this case it is safe because BFS checks in the order of distance, basically every state which is one move away from the start state gets taken off the queue first
# before a state which is two away etc. So, the first time that BFS reaches a state it will have come by fewest moves as every move counts for 1
# so its the shortest distance and doesnt change.
# Using minutes then roads would have different lengths whichmeans a route (Galway to Roundstone - BFS reaches it via spiddal first and records 105 mins, however, the quickest route is 70 via Oughterard and Recess) 
# with fewest roads does not mean it takjes the quickest time. BFS records the minutes for the route it reaches first and wouldn't update this. if we want to find the quickets route based on time and not roads then
# we would need to use weighting and this needs a dijksta algorthim as it would check cheapest (in terms of time) and updates it when a cheaper route is found.
