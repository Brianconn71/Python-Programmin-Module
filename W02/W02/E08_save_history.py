"""Extension. Keep your keypresses, so you can experiment on them later.

Run the tests:

    python -m doctest W02/E08_save_history.py

No output means every test passed.

The lecture saved the *model* (the n-gram counts). This saves the *data* (what
you actually typed), which is more useful: from the data you can rebuild any
model you like, but from a model you cannot get the data back.

One line per session, so playing again adds to the file rather than replacing
it. E09_ngram_sweep.py reads what this writes.

Note each test below cleans up its own file at the end. Doctests run in
alphabetical order by function name, not the order they appear in the file, so
no test may depend on another having run first.
"""

from pathlib import Path

DATA = Path(__file__).parent / "data"


def history_path(student_id):
    """Return the file this student's sessions are saved in.

    >>> history_path("12345678").name
    'history_12345678.txt'

    It sits next to this source file, not next to wherever you ran python:

    >>> history_path("12345678").parent.name
    'data'
    """
    # using the DATA global variable which is the path to the data folder inside Wo2
    # I am then adding a new file to this folder with history and student id number. as a txt file
    pathfile = DATA / f"history_{student_id}.txt"

    # I am then returning the path this file is on.
    return  pathfile


def save_history(history, student_id):
    """Append one session to this student's file, as a single line.

    Use mode "a", not "w": a second session must not delete the first.

    >>> save_history("fdfd", "testA")
    >>> save_history("ddff", "testA")
    >>> print(open(history_path("testA")).read(), end="")
    fdfd
    ddff
    >>> history_path("testA").unlink()
    """
    # Open the file in append mode and adding the history to the file
    # with Open opens the file and when that block ends the file gets closed
    with open(history_path(student_id), "a") as file:
        # Writing the historyto the student ID file as a new line.
        file.write(history + "\n")


def load_histories(student_id):
    """Return this student's sessions, oldest first, as a list of strings.

    Each line of the file is one session. Strip the newline off the end.

    >>> save_history("fdfd", "testB")
    >>> save_history("ddff", "testB")
    >>> load_histories("testB")
    ['fdfd', 'ddff']
    >>> history_path("testB").unlink()

    A student who has never played has no file, and so no sessions. That is
    not an error:

    >>> load_histories("nobody_at_all")
    []
    """
    # using a try except block because if a student has no file they have no sessions and no file is found in the folder
    # FileNotFoundError gets returned so I am accounting for this by not returning the actual error itself but an empty list which is whats expected.
    try:
        # Open the file in read mode
        with open(history_path(student_id), "r") as file:
            # reading the file and removing the new lines from the file
            load_history = file.read().splitlines()
        # values then get returned to us in a list
        return  load_history
    # file not found error for when a student has no sessions, its a great way to overcome errors as it lets you return a default value
    # when the file is not found
    except FileNotFoundError:
        # return an empty list.
        return []


def total_keys(student_id):
    """How many keypresses this student has contributed, over all sessions.

    >>> save_history("fdfd", "testC")
    >>> save_history("ddffdd", "testC")
    >>> total_keys("testC")
    10
    >>> history_path("testC").unlink()

    >>> total_keys("nobody_at_all")
    0
    """
    # Initialize count variable at 0
    count = 0
    
    # loop through the values we get inside the list returned from the function load_histories
    for value in load_histories(student_id):
        # count is then equal to the length of the characters inside the value
        count += len(value)
    # We return this count value.
    return count
