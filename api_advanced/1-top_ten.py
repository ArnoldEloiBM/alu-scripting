#!/usr/bin/python3
""" top_ten.py """
import requests

def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed for a given subreddit. """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Chrome/1.0'}

    # Make the request and prevent redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
    except ValueError:
        print(None)
        return

    # Extract and print the titles of the first 10 hot posts
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        print(post.get('data', {}).get('title'))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])