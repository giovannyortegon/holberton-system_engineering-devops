#!/usr/bin/python3
""" Impoprts """
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """ recursive function that queries the Reddit API
        and returns a list containing the titles of all
        hot articles for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'skillhh'}
    data = {'limit': 100, 'after': after}

    req = get(url, headers=header, params=data, allow_redirects=False)

    if req.status_code >= 400:
        return None
    else:
        resps = req.json().get('data').get('children')
        for resp in resps:
            hot_list.append(resp.get('data').get('title'))

        dates = req.json().get('data').get('after')
        if dates is not None:
            recurse(subreddit, hot_list, dates)
        return hot_list
