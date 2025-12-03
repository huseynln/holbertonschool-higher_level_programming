#!/usr/bin/python3
"""34234"""

import json


def save_to_json_file(my_obj, filename):
    """3242"""

    with open(filename, "w") as mf:
        json.dump(my_obj, mf)
