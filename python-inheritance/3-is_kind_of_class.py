#!/usr/bin/python3
"""Module that defines is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or inherited from, a_class

    Args:
        obj: Any Python object
        a_class: A class to check against

    Returns:
        True if obj is an instance of a_class or a subclass of a_class,
        False otherwise
    """
    return isinstance(obj, a_class)
