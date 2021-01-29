#!/usr/bin/python3
"""x"""
import requests


def recurse(subreddit, h_l=[], after=""):
    """asks reddit nicely for some info"""
    h = {"User-Agent": "Reddit Scraper"}
    p = {"after": after}
    url = "https://www.reddit.com/r/{}/hot.json?limit=1"
    raw = requests.get(url.format(subreddit), headers=h, params=p)
    if not raw:
        return None
    out = raw.json()
    after = out.get("data").get("after")
    if not after:
        return h_l
    h_l.append(out.get("data").get("children")[0].get("data").get("title"))
    return recurse(subreddit, h_l, after)
