#!/usr/bin/python3
"""4324"""

import json


def load_from_json_file(filename):
    """2343"""

    with open(filename, "r") as mg:
        return json.load(mg)
