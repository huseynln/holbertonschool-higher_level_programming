#!/usr/bin/python3
"""3243"""


def append_write(filename="", text=""):
    """@34324"""

    with open(filename, "a") as mf:
        mf.write(text)
    return len(text)
