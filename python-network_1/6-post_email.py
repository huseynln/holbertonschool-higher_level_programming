#!/usr/bin/python3
""" fsaf """

import requests as req
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    data = {"email": mail}
    r = req.post(url, data)
    print(r.text)
