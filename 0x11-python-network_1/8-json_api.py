#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    result = requests.post(url, data={"q": letter})

    try:
        response = result.json()
        if not response:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")

    except Exception:
        print("Not a valid JSON")
