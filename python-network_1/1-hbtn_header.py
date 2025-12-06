#!/usr/bin/python3
""" fsadfds"""


import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
