"""Extension. Sorting the photos from darkest to brightest.

Run the tests:

    python -m doctest W08/E07_brightness.py

No output means every test passed. Then run the file itself, which needs
the photos:

    python prep_data.py
    python E07_brightness.py

A photo's brightness is just the mean of all its numbers, across height,
width and all three colour channels at once. Sorting by it introduces the
other half of argsort: it hands you the *order*, and you then use that order
to index something else. Indexing one array with an array of positions is
called fancy indexing, and it is how a sorted list of names is built here.
"""
import numpy as np

# Needed to add this line as was having issues with numpy versions
# I had numpy 2.5 installed, newer numpy does not need np.int64(1)
np.set_printoptions(legacy="1.25")

from E01_photos import DATA, load


def brightness(image):
    """The mean of every number in the image, as an ordinary float.

    >>> image = np.array([[[0, 0, 0], [255, 255, 255]]], dtype=np.uint8)
    >>> brightness(image)
    127.5
    >>> brightness(np.zeros((4, 4, 3), dtype=np.uint8))
    0.0
    """
    # using mean numpy method to get the mean of every number in the image
    # when using mean without an axis argument of 1 or 0 then numpy will treat the whole array
    # as one flat list of numbers regardless of rows and columns. if using axes then numpy will collapse that axis into one dimension but leave other as is 
    # this then returns an array of means and not a single number
    # wrapping my numpy mean value in a float method which turns it into an ordinary float 
    # we then return this to the user
    return float(image.mean())


def darkest_first(names, values):
    """Return the names as an array, reordered from smallest value to largest.

    np.argsort(values) gives the positions in sorted order; use that array to
    index the names.

    >>> darkest_first(["a", "b", "c"], [5.0, 1.0, 3.0])
    array(['b', 'c', 'a'], dtype='<U1')
    >>> darkest_first(["a", "b", "c"], [1.0, 2.0, 3.0])
    array(['a', 'b', 'c'], dtype='<U1')
    """
    # using argsort on values input argument to get the positions from smallest to largest
    valuesSorted = np.argsort(values)
    # names input is a regular python list and fancy indexing does not work on python lists
    # so I turn it into a numpy array using np.array on the names input argument
    namesArray = np.array(names)
    # now, using the sorted positions on the created names array
    # this is used to create a new array of the names in the order of the sorted values
    reorderedList = namesArray[valuesSorted]
    # we then return this new array with the names reordered from smallest to largest to the user
    return reorderedList


def main():
    paths = sorted((DATA / "photos").glob("*full.png"))
    if not paths:
        print("No photos yet. Run:  python prep_data.py")
        return
    values = [brightness(load(p)) for p in paths]
    order = darkest_first([p.stem for p in paths], values)
    if order is None:
        print("write brightness and darkest_first first")
        return
    print("darkest: ", order[:3])
    print("brightest:", order[-3:])


if __name__ == "__main__":
    main()
    darkest_first(["a", "b", "c"], [5.0, 1.0, 3.0])
