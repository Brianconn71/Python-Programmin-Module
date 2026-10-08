"""Extension. Carrying information down the recursion.

Run the tests:

    python -m doctest W03/E07_part_paths.py

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


def part_paths(node, prefix=""):
    """Return the full path of every part you buy, deepest name last.

    Everything so far has passed answers back up the tree. This passes
    something down: each call builds the path of the node it is looking at
    and hands it to its children, exactly as depth was handed down in the
    lecture's debugging version of unit_mass.

    prefix is where the caller is; do not set it yourself when you call
    part_paths from outside.

    >>> for path in part_paths(bicycle):
    ...     print(path)
    bicycle/wheel/rim
    bicycle/wheel/spoke
    bicycle/wheel/hub
    bicycle/wheel/tyre
    bicycle/frame
    bicycle/handlebar
    bicycle/saddle
    bicycle/chain

    The path of a part depends on where you started, not on where it lives:

    >>> part_paths(bicycle["children"][0])
    ['wheel/rim', 'wheel/spoke', 'wheel/hub', 'wheel/tyre']
    >>> part_paths(bicycle["children"][1])
    ['frame']
    """
    # Initialize a path variable with the prefix - which is passed down 
    # it carries the path thats been created so far down the recursion.
    # this is initialised as a string
    path = prefix + node["name"]

    # if there are children then its not a part we buy its a part we make
    # so, we return the path sent to us as an argument back to the user.
    # Path is stored as a string so we cover with square brackets to turn into a
    # list object.
    if "children" not in node:
        return [path]

    # another path variable for collecting paths handed down and stored
    additionalPath = []

    # for loop for all the values in the children list of dicts.
    for value in node["children"]:
        # adding the handed down path to list vvariable with the path in the input argument along with the value of the current path separated with a /
        additionalPath += part_paths(value, path + "/")
    # then, return this valeu to user.
    return additionalPath


def find_part(node, path):
    """Return the part at the given path, or raise KeyError if there is none.

    >>> find_part(bicycle, "bicycle/wheel/hub")["mass"]
    200
    >>> find_part(bicycle, "bicycle/frame")["material"]
    'steel'
    >>> find_part(bicycle, "bicycle")["name"]
    'bicycle'
    >>> find_part(bicycle, "bicycle/wheel/axle")
    Traceback (most recent call last):
        ...
    KeyError: 'bicycle/wheel/axle'
    """
    # creating a list of the input argument path string values split by /
    # path_names will contain a list of the calues from path split where the / was.
    path_names = path.split("/")
    # current Node is the node / dictionary we are using as an input argument.
    currentNode = node

    # Looping through the name values from our path but skipping the first value Bicycle
    # because bicycle is at the root of the dictionary / path and no more values to be passed down from it.
    for name in path_names[1:]:
        # Children is a dict comprehension storing the name of the children parts as keys and there values as the value in the new dict.abs
        # get will return an empty list if the key doesnt exist
        children = {x["name"]: x for x in currentNode.get("children", [])}
        # if this iteration name value is not in the newly created children dictionary
        if name not in children:
            # then we have an error and we raise the key error back to the user with the path value they have added as input.
            raise KeyError(path)
        # then current node is set as the value of the name value from the newly created children dictionary
        currentNode = children[name]
    # then we return this value to the user.
    return currentNode
