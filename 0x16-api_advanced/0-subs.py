#!/usr/bin/python3
"""
    a function that queries the Reddit API and
    returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    link = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(link, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
