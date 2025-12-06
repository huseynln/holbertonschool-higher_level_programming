#!/usr/bin/python3


import requests as req
import csv


url = "https://jsonplaceholder.typicode.com/posts/"

def fetch_and_print_posts():
    try:
        r = req.get(url)
        print(f"Status Code: {r.status_code}")
        for i in r.json():
            print(i["title"])
    except Exception:
        raise Exception
def fetch_and_save_posts():
    try:
        r = req.get(url)
        posts = r.json()
        keys = ["id", "title", "body"]
        filtered_posts = [{field: post[field] for field in keys} for post in posts]
        with open("posts.csv", "w", newline="", encoding="utf-8") as mf:
            writer = csv.DictWriter(mf, fieldnames=keys)
            writer.writeheader()
            writer.writerows(filtered_posts)

    except Exception:
        raise Exception
