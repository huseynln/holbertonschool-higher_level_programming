#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value.

    Args:
        a_dictionary: Dictionary with integer values

    Returns:
        The key with the highest value, or None if no score found
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    return max(a_dictionary, key=a_dictionary.get)
