#!/usr/bin/python3
"""takes in a URL, sends a request to the URL, displays the value"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        content = response.info().get("X-Request-Id")
        print(content)
