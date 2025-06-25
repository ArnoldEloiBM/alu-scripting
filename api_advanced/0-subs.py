#!/usr/bin/python3
"""Query Reddit API for subreddit subscriber count"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    Args:
        subreddit (str): The subreddit to query
    Returns:
        int: Number of subscribers or 0 if invalid subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditBot/0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        return 0
    except Exception:
        return 0
