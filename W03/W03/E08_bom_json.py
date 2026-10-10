"""Extension. The bill of materials as a file you can change.

Run the tests:

    python -m doctest W03/E08_bom_json.py

No output means every test passed.
"""

import json
from pathlib import Path

DATA = Path(__file__).parent / "data"


# Given: unit_mass from the lecture, with the extra argument promised there.
# key says which number to add up, so the same function weighs or prices.
# You do not need to change it.
def everything(node):
    return True


def unit_total(node, key="mass", keep=everything):
    """Total node[key] over one of node, counting only parts keep() accepts."""
    if "children" not in node:
        return node[key] if keep(node) else 0
    return sum(c["qty"] * unit_total(c, key, keep) for c in node["children"])


def load_bom(filename):
    """Read a bill of materials from a JSON file in the data folder.

    >>> bom = load_bom("bicycle.json")
    >>> bom["name"]
    'bicycle'
    >>> round(unit_total(bom, key="cost"), 2)
    279.6
    """
    # Creating a new variable file to hold the Path to the file already defined on line 13
    # with the filename added by the user in this case bicycle.json
    # A new filepath is created with the filename added and we can then find the file in our directory for working with.
    file = DATA / filename

    # Using with to open the json file and store as variable f
    with open(file) as f:
        # Using json.load method to read the json file into dicts and lists in this case.
        return json.load(f)


def repriced(node, material, factor):
    """Return a new tree with the cost of every `material` part multiplied.

    The tree that was passed in must not be changed: the supplier's price
    rise is a new version of the bill of materials, not an edit of the one
    already in memory. So build a new dict at every level rather than
    assigning into the old one.

    >>> bom = load_bom("bicycle.json")
    >>> dearer = repriced(bom, "steel", 1.10)
    >>> round(unit_total(dearer, key="cost"), 2)
    295.46

    Everything else is untouched -- the masses, and the parts made of
    anything but steel:

    >>> unit_total(dearer) == unit_total(bom)
    True
    >>> round(unit_total(bom, key="cost"), 2)
    279.6
    """
    # creating an exact copy of the input node in a completely separate dictionary
    # this way the original node stays the same and we can make changes to the new node.
    new_node = dict(node)

    # means that this is a part that we buy.
    # if there are children in this node then, parts will have no children as a key
    # jump over the if statements and run the list comprehension below calling repriced
    # with the new item in the node children.
    # this is the base case
    if "children" not in node:
        # is this part material equal to the material we are adding as an input argument?
        if node["material"] == material:
            # if it is then we change the value of the field cost in the new dictionary
            # To equal the value from the input dictionary times the factor input argument.
            new_node["cost"] = node["cost"] * factor
        # The return the part regardless of if it was correct material or not to the new node dict.
        return new_node

    # This is where the recursion takes place, it is the recursive case
    # Builds a new list object by calling repriced on every child
    # returns a new copy of the reprice call on the child which may have additional dictionaries within it
    new_node["children"] =  [repriced(c, material, factor) for c in node["children"]]

    # returning the newly created node as a dictionary.
    return  new_node


def save_bom(bom, path):
    """Write a bill of materials out as JSON.

    json.dump writes to an open file, so it needs a `with` block just as
    reading did. indent=4 makes the file readable by a human as well as by
    a program.

    A round trip through a file should change nothing at all:

    >>> import tempfile
    >>> bom = load_bom("bicycle.json")
    >>> dearer = repriced(bom, "steel", 1.10)
    >>> path = Path(tempfile.mkdtemp()) / "dearer.json"
    >>> save_bom(dearer, path)
    >>> with open(path) as f:
    ...     reloaded = json.load(f)
    >>> reloaded == dearer
    True
    >>> round(unit_total(reloaded, key="cost"), 2)
    295.46
    """
    return  # YOUR CODE HERE

if __name__ == "__main__":
    bom = load_bom("bicycle.json")
    dearer = repriced(bom, "steel", 1.10)
