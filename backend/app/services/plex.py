from typing import Annotated, cast

from fastapi import Depends
from plexapi.base import MediaContainer
from plexapi.server import PlexServer
from plexapi.video import EpisodeHistory

from app.config import AppConfig


def get_plex_server(config: AppConfig):
    return PlexServer(config.plex_url, config.plex_token)


PlexClient = Annotated[PlexServer, Depends(get_plex_server)]


def get_recently_watched(plex: PlexClient):
    history: MediaContainer[EpisodeHistory] = cast(
        MediaContainer[EpisodeHistory], plex.history()
    )
    if not history:
        return []

    watched = {}

    for item in history:
        key = item.grandparentTitle if hasattr(item, "grandparentTitle") else item.title
        if not key:
            continue
        found = watched.get(key)
        if found:
            found["episodes_watched"] += 1
        else:
            watched[key] = {
                "title": item.title if item.title else item.grandparentTitle,
                "episodes_watched": 1,
            }

    return list(watched.values())
