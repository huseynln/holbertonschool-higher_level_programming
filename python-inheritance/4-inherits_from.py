#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from a_class

    Returns False if obj is exactly an instance of a_class

    Args:
        obj: Any Python object
        a_class: A class to check against

    Returns:
        True if obj's class inherited (directly or indirectly) from a_class,
        False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
