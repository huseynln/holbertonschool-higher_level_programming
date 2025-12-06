#!/usr/bin/python3
""" fsaf """


import urllib.request as ureq
import sys
import urllib.parse as upar


if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    data = {"email": mail}
    data = upar.urlencode(data)
    data = data.encode("ascii")
    request = ureq.Request(url, data)
    with ureq.urlopen(request) as res:
        print(res.read().decode("utf-8"))
