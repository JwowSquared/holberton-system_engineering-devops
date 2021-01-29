#!/usr/bin/python3
"""x"""
import requests


def number_of_subscribers(subreddit):
    """asks reddit nicely for some info"""
    headers = requests.utils.default_headers()
    headers.update({"User-Agent": "Reddit Scraper"})
    url = "https://www.reddit.com/r/{}/about.json"
    raw = requests.get(url.format(subreddit), headers=headers).json()
    out = raw.get("data").get("subscribers")
    if out:
        return out
    return 0
