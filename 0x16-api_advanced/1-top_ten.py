#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/111.0.0.0 Safari/537.36'}
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data')
        articles = data.get("children")
        for article in articles:
            data = article.get("data")
            print(data.get("title"))
    else:
        print(None)
