#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    password = sys.argv[2]
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {password}"
    }

    result = requests.get(url, headers=headers)

    response = result.json()
    if response:
        print(f"{response.get('id')}")
