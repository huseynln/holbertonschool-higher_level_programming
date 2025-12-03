#!/usr/bin/python3
""" 434 """


import csv
import json

def convert_csv_to_json(filename):
    """ 43 """
    try:
        with open(filename, "r") as mf:
            data = list(csv.DictReader(mf))
        with open("data.json", "w") as mf:
            json.dump(data, mf)
        return True
    except Exception:
        return False
