#!/usr/bin/python3
""" Imports """
from requests import get


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API
        and returns the number of subscribers.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'skillhh'}
    req = get(url, headers=header, allow_redirects=False)

    if req.status_code == 200:
        resp = req.json().get('data')
        subscribters = resp.get('subscribers')
        return subscribters
    else:
        return 0
