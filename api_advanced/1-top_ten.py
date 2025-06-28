#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'python:reddit.topten:v1.0 (by /u/YourRedditUsername)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json()['data']['children']
            for post in posts[:10]:  # Ensure we only take 10 posts
                print(post['data']['title'])
        else:
            print(None)
    except Exception:
        print(None)