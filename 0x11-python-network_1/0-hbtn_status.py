#!/usr/bin/python3

from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as res:
        body = res.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
