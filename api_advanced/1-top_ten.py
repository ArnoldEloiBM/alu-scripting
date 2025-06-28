#!/usr/bin/python3
"""
Function that queries Reddit API and prints titles of first 10 hot posts for a given subreddit.
If subreddit is invalid, prints None.
"""

import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)