#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.

    Args:
        a_dictionary: The dictionary to delete from
        key: The key to delete (always a string)

    Returns:
        The dictionary with the key deleted (if it existed)
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
