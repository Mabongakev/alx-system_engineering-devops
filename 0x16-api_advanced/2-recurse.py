#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit."""
from requests import get

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches hot post titles from a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "MyRedditBot/1.0"
    }
    params = {
        "limit": 100,  
        "after": after  
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None  

    data = response.json()
    posts = data.get("data", {}).get("children", [])

   
    for post in posts:
        hot_list.append(post["data"]["title"])

   
    after = data["data"].get("after")
    if after:
        return recurse(subreddit, hot_list, after)
