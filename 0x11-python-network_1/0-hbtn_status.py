#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('UTF-8')}")
