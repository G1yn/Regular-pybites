from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    root = feedparser.parse(FEED_URL)
    mylist = []
    for i, entry in enumerate(root.entries):
        mylist.append(Game(root.entries[i].title, root.entries[i].link))

    return mylist
