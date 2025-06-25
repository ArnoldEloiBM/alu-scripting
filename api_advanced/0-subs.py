#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/0.0.1'}

    # Construct the URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Make the request, allowing redirects but checking the final URL
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid by ensuring no redirect and status code 200
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
