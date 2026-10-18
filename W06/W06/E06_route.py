"""Extension. What "fewest roads" costs you, in minutes.

Run the tests:

    python -m doctest W06/E06_route.py

No output means every test passed.

`E01_river.py` has both searches in it already: `bfs_graph`, which minimises
the number of edges, and `dijkstra`, which minimises the total weight. Run
both on `ROADS` and the difference between them is a number of minutes.
"""

from E01_river import ROADS, bfs_graph, dijkstra, road_time, roads_from


def time_lost(start, goal):
    """How many minutes the fewest-roads route costs you over the quickest.

    Zero where the two searches happen to agree, which is most of this map.

    >>> time_lost("Galway", "Roundstone")
    35
    >>> time_lost("Cong", "Carna")
    35
    >>> time_lost("Galway", "Clifden")
    0
    >>> time_lost("Galway", "Galway")
    0
    """
    # first we check to make sure there is a route from a -> b
    # bfs_graph will return the route as a list of towns/values if true and None if no route exists.
    # This is more of a precaution than anything
    graph = bfs_graph(ROADS, start, goal)
    if graph:
        # Once we know a route exists we call dijkstra function with the start, the goal which are added as inputs to function along with
        # the roads_from function imported which is a successor funtion to ROADS dictionary and returns the items from the roads dictionary which we are adding as input start
        # dijkstra then returns a tuple pair with the cost and the route as a list
        cost, route = dijkstra(roads_from, start, goal)
        # Then we calculate the time on the road we spent with a bfs_graph
        # We call road_time which takes in the list of values we got from the bfs_graph and gives back how long the route took in mins
        timeOnRoads = road_time(graph)
        # so now we return the length of time using bfs_graph minus the length of time using dijksta and return to user.
        # reason for this way is because dijkstra gets the cheapest route whereas bfs gets the shortest route.
        return timeOnRoads - cost
    else:
        # SHould probably return an error here but thats not what is asked of the function.
        return 0


def quickest_times(start):
    """The quickest time from `start` to every town on the map, as a dict.

    >>> times = quickest_times("Galway")
    >>> times["Roundstone"]
    70
    >>> times["Clifden"]
    72
    >>> times["Galway"]
    0
    >>> len(times) == len(ROADS)
    True

    >>> quickest_times("Clifden")["Galway"]
    72
    """
    return  # YOUR CODE HERE

if __name__ == "__main__":
    time_lost("Galway", "Galway")