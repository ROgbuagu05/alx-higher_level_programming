#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        response = respnse.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
