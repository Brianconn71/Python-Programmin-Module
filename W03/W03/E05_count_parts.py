"""Composition. The same walk down the tree, a different question.

Run the tests:

    python -m doctest W03/E05_count_parts.py

No output means every test passed.
"""

# Given: the bicycle from the lecture. You do not need to change it.
bicycle = {
    "name": "bicycle", "qty": 1, "children": [
        {"name": "wheel", "qty": 2, "children": [
            {"name": "rim",   "qty": 1,  "material": "aluminium", "mass": 380},
            {"name": "spoke", "qty": 32, "material": "steel",     "mass": 5},
            {"name": "hub",   "qty": 1,  "material": "steel",     "mass": 200},
            {"name": "tyre",  "qty": 1,  "material": "rubber",    "mass": 320},
        ]},
        {"name": "frame",     "qty": 1, "material": "steel",     "mass": 2200},
        {"name": "handlebar", "qty": 1, "material": "aluminium", "mass": 300},
        {"name": "saddle",    "qty": 1, "material": "plastic",   "mass": 260},
        {"name": "chain",     "qty": 1, "material": "steel",     "mass": 300},
    ],
}


def count_parts(node):
    """Return how many physical parts are inside one of node.

    The lecture's parts() returned one dict per line in the bill, eight of
    them. This counts the things you would actually unpack from the box.
    A part you buy is one part; a part you build is everything inside it,
    each child counted qty times -- the same shape as unit_mass.

    >>> count_parts(bicycle)
    74
    >>> count_parts(bicycle["children"][0])       # one wheel: rim, 32 spokes, hub, tyre
    35
    >>> count_parts(bicycle["children"][0]["children"][1])   # one spoke
    1
    """

    #if "qty" in node:
     #       return node["qty"] if keep(node) else 0
    #return sum(c["qty"] * unit_mass(c, keep) for c in node["children"])
    # initialize a counter
    count = 0
    # if the material field is in the dictionary then we know we have a specific part which has a quantity to be added.
    if "material" in node:
        return 1
    
    # for the value in the loop which is a list of a nodes children
    for value in node["children"]:
        # we are adding the count with the value for the field qty times the amount of parts in the node.
        count += value["qty"] * count_parts(value)

    # returnng the count of the parts.
    return count


def deepest(node):
    """Return how many levels deep the tree goes. A single part is depth 0.

    Nothing accumulates on the way down here: each call asks its children
    how deep they are and takes the largest answer, plus one for itself.

    >>> deepest(bicycle)
    2
    >>> deepest(bicycle["children"][0])
    1
    >>> deepest(bicycle["children"][1])
    0
    """
    count = 0

    for value in node:
        print(value)
        if isinstance(value, list):
            count +=  deepest(value)

    return  count
