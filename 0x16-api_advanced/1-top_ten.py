#!/usr/bin/python3
"""
    a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    link = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    paramet = {"limit": 10}
    response = requests.get(link, headers=headers, params=paramet,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
