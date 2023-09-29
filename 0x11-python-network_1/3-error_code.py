#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body"""
import sys
import urllib.request
import urllib.parse
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            result = response.read()
            print(result.decode('UTF-8'))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
