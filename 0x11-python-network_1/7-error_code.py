#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
"""

import sys
from requests import get

if __name__ == "__main__":
    req = get(sys.argv[1])

    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
