#!/usr/bin/python3
"""This connects to a github account and print the latest commits"""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits"
    req = requests.get(url)
    temp = []
    if len(req.json()) > 10:
        temp += req.json()[0:10]
    else:
        temp += req.json()
    for val in temp:
        line = f"{val['sha']}: {val['commit']['author']['name']}"
        print(line)
