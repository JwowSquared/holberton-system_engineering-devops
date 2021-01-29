#!/usr/bin/python3
"""x"""
import requests


def number_of_subscribers(subreddit):
    """asks reddit nicely for some info"""
    h = {"User-Agent": "Reddit Scraper"}
    url = "https://www.reddit.com/r/{}/about.json"
    raw = requests.get(url.format(subreddit), headers=h, allow_redirects=False)
    out = raw.json().get("data").get("subscribers")
    if out:
        return out
    return 0
