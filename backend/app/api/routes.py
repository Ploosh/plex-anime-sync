from typing import Any

from fastapi import APIRouter

from app.services import plex

# from app.services.mal import update_anime_from_plex

router = APIRouter()


@router.get("/sync")
def sync_watched(plex_client: plex.PlexClient) -> dict[str, list[dict[str, Any]]]:
    results = plex.get_recently_watched(plex_client)
    return {"recently_watched": results}
    # updates = update_anime_from_plex(results)
    # return {"synced": updates}


# @router.get("/auth/callback")
# def mal_callback(code: str):
#     token_info = exchange_code_for_token(code)
#     return token_info
