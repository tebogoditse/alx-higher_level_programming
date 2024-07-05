#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

from requests import get

if __name__ == "__main__":
    req = get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")
