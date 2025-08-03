from plexapi.server import PlexServer
import os

def get_recently_watched():
    plex = PlexServer(os.getenv("PLEX_URL"), os.getenv("PLEX_TOKEN"))
    history = plex.account().watchHistory()
    return [
        {
            "title": item.title,
            "episodes_watched": 1,
            "rating": 8  # hardcoded or inferred
        }
        for item in history if 'anime' in item.librarySectionTitle.lower()
    ]
