#!/usr/bin/python3
"""Improved version combining both approaches"""
import requests


def top_ten(subreddit):
    """Prints top 10 hot posts or None if invalid subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'MyRedditBot/0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    except Exception:
        print(None)
