#!/usr/bin/python3
"""
Script that takes in a URL,
sends a request to the URL and displays the value of the X-Request-Id
"""

import sys
from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request(sys.argv[1])
    with urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
