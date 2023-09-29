#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL, display"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    result = requests.get(url)

    if result.status_code < 400:
        print(result.text)
    else:
        print(f"Error code: {result.status_code}")
