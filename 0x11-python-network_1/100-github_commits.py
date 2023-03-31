#!/usr/bin/python3
"""This connects to a github account and print the latest commits"""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"
    req = requests.get(url).json()
    try:
        for i in range(10):
            print("{}: {}".format(
                req[i].get("sha"),
                req[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
