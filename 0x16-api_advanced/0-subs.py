#!/usr/bin/python3

"""
Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests,
ensure you’re setting a custom User-Agent.

Requirements:
    - Prototype: def number_of_subscribers(subreddit)
    - If not a valid subreddit, return 0.
    - Note: Invalid subreddits may return a redirect to search results.
      Ensure that you are not following redirects.
"""


from requests import get


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers in a subreddit

    Params:
        subreddit (str): The name of the subreddit

    Return:
        The number of subscribers if the subreddit exists, 0 otherwise
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    response = get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        allow_redirects=False)

    if response.ok:
        try:
            subscriber_count = response.json().get('data').get('subscribers')
        except Exception:
            return 0

    return subscriber_count
