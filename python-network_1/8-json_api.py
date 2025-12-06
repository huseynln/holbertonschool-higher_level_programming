#!/usr/bin/python3
""" 545443 """


import requests as req
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) == 2:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    r = req.post(url, data={"q": q})
    try:
        if len(r.json()) == 0:
            print("No result")
        else:
            print(f"[{r.json()['id']}] {r.json()['name']}")
    except req.exceptions.JSONDecodeError:
        print("Not a valid JSON")
