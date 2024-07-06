#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import sys
from requests import get
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = get("https://api.github.com/user", auth=auth)

    print(req.json().get("id"))
