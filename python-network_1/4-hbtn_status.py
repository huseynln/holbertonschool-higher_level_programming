#!/usr/bin/python3
""" 3543 """


import requests as req


if __name__ == "__main__":
    myreq = req.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(myreq.text)}")
    print(f"\t- content: {myreq.text}")
