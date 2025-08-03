from typing import Annotated, cast

from fastapi import Depends
from plexapi.base import MediaContainer
from plexapi.library import ShowSection
from plexapi.server import PlexServer
from plexapi.video import EpisodeHistory

from app.config import AppConfig


def get_plex_server(config: AppConfig):
    return PlexServer(config.plex_url, config.plex_token)


PlexClient = Annotated[PlexServer, Depends(get_plex_server)]


def get_animes(plex: PlexClient):
    """
    Fetches all anime from the Plex server.
    """
    animes = cast(ShowSection, plex.library.section("Anime"))
    if not animes:
        return []

    return [
        {
            "title": anime.title,
            "key": anime.key,
            "ratingKey": anime.ratingKey,
            "summary": anime.summary,
            "year": anime.year,
        }
        for anime in animes.all()
    ]


def get_recently_watched(plex: PlexClient):
    history: MediaContainer[EpisodeHistory] = cast(
        MediaContainer[EpisodeHistory],
        plex.history(librarySectionID=plex.library.section("Anime").key),
    )
    if not history:
        return []

    watched = {}

    for item in history:
        key = item.key
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
