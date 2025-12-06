#!/usr/bin/python3
""" 3543 """


import requests as req
import sys


if __name__ == "__main__":
    try:
        myreq = req.get(sys.argv[1])
        myreq.raise_for_status()
        print(f"{myreq.text}")
    except req.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
