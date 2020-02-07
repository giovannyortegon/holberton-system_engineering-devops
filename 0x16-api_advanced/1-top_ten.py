#!/usr/bin/python3
""" Imports """
from requests import get


def top_ten(subreddit):
    """ Queries the Reddit API and prints the titles
        of the first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'skillhh'}

    req = get(url, headers=header, allow_redirects=False)

    if req.status_code >= 300:
        print('None')
    else:
        resps = req.json().get('data').get('children')
        for resp in resps:
            print(resp.get('data').get('title'))
