#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit"""
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}"\
            .format(subreddit, after)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/111.0.0.0 Safari/537.36'}
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get("after")
        articles = data.get("children")
        for article in articles:
            hot_list.append(article)
        recurse(subreddit, hot_list, after)

    if len(hot_list) == 0:
        return None
    return hot_list
