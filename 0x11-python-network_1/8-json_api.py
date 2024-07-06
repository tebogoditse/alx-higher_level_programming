#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
from requests import post

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payLoad = {"q": letter}
    req = post("http://0.0.0.0:5000/search_user", payLoad)

    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print(f"[{res.get('id')}] {res.get('name')}")
    except ValueError:
        print("Not a valid JSON")
