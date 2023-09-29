#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    result = requests.get(url).text
    print("Body response:")
    print(f"\t- type: {type(result)}")
    print(f"\t- content: {result}")
