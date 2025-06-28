#!/usr/bin/python3
""" recurse.py """
import requests

def recurse(subreddit, hot_list=None, after=None):
    """ Recursively queries the Reddit API and returns a list of titles of all hot articles for a given subreddit. """
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Chrome/1.0'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
    except ValueError:
        return None

    posts = data.get('data', {}).get('children', [])
    for post in posts:
        hot_list.append(post.get('data', {}).get('title'))

    after = data.get('data', {}).get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")