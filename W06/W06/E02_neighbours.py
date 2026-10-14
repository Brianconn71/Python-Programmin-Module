"""Drill. Read a graph out of a dict, whatever shape the dict is.

Run the tests:

    python -m doctest W06/E02_neighbours.py

No output means every test passed.

`E01_river.py` has two graphs in it, and they are not stored the same way.
`RIVER_GRAPH` maps a state to a *list* of states; `ROADS` maps a town to a
*dict* of town -> minutes. All three functions here work on both, because
iterating a dict gives you its keys.
"""

from E01_river import RIVER_GRAPH, ROADS


def neighbours(graph, node):
    """Which nodes is `node` joined to? Sorted, so the answer is predictable.

    An empty list if we have never heard of the node, rather than a KeyError.

    >>> neighbours(ROADS, "Galway")
    ['Oughterard', 'Spiddal']
    >>> neighbours(RIVER_GRAPH, "LLRL")
    ['RLRL', 'RLRR', 'RRRL']
    >>> neighbours(ROADS, "Dublin")
    []
    """
    # Using a try except block to catch KeyErrors and if keyerror arises it will return an empty list.
    try:
        # New list to store the vales from the input graph once we are looping through its contents values get stored here
        nodeValuesList = []
        # if the node actually appears in the graph given as input, if it doesnt the except block will capture the keyerror
        # and return an empty list in its place.
        if node in graph:
            # loop through the values of our graph based on the input node as we know its in the graph itself.
            # using sorted here to sort the values of the dict/list in place before we append the value to the new list created
            for value in sorted(graph[node]):
                # Now, we take the value from the inner graph(dict(keys)/list(values)) and append to the new list 
                nodeValuesList.append(value)
    # Deals with keyerrors, as in input values which don't appear in the graph provided.
    except KeyError:
        # return an empty list rather than a KeyError
        return []
    # Once the function has finished looping and the new list has its values, we then return this to the user
    return  nodeValuesList


def is_edge(graph, a, b):
    """Is there an edge from `a` to `b`?

    >>> is_edge(ROADS, "Galway", "Oughterard")
    True
    >>> is_edge(ROADS, "Galway", "Clifden")
    False
    >>> is_edge(ROADS, "Dublin", "Galway")
    False
    """
    return  # YOUR CODE HERE


def degree(graph, node):
    """How many edges does `node` have?

    >>> degree(ROADS, "Roundstone")
    3
    >>> degree(RIVER_GRAPH, "LLLL")
    1
    """
    return  # YOUR CODE HERE

if __name__ == "__main__":
    neighbours(ROADS, "Galway")