#!/usr/bin/python3
"""Module that defines a lookup function"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: Any Python object

    Returns:
        A list of strings representing attributes and methods
    """
    return dir(obj)
