#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"Your email is: {}".format(sys.argv[2])}
    data = urlencode(value).encode("ascii")
    req = Request(url, data)

    with urlopen(req) as res:
        print(res.read().decode("uft-8"))
