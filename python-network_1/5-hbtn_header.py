#!/usr/bin/python3
""" 3543 """


import requests as req
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    myreq = req.get(url)
    print("{}".format(myreq.headers["X-Request-Id"]))
