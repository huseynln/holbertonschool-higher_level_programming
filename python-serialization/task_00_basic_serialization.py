#!/usr/bin/python3
"""42342"""


import json


def serialize_and_save_to_file(data, filename):
    """3243"""

    with open(filename, "w") as mf:
        json.dump(data, mf)

def load_and_deserialize(filename):
    """343"""

    md = {}
    with open(filename, "r") as mf:
         md = json.load(mf)
    return md
