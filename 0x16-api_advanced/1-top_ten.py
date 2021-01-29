#!/usr/bin/python3
"""x"""
import requests


def top_ten(subreddit):
    """asks reddit nicely for some info"""
    h = {"User-Agent": "Reddit Scraper"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10"
    raw = requests.get(url.format(subreddit), headers=h)
    if not raw:
        print(None)
        return
    out = raw.json().get("data").get("children")
    if out:
        for hot in out:
            print(hot.get("data").get("title"))
    else:
        print(None)
