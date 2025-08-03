from fastapi import APIRouter
from app.services.plex import get_recently_watched
from app.services.mal import update_anime_from_plex

router = APIRouter()

@router.get("/sync")
def sync_watched():
    results = get_recently_watched()
    updates = update_anime_from_plex(results)
    return {"synced": updates}

@router.get("/auth/callback")
def mal_callback(code: str):
    token_info = exchange_code_for_token(code)
    return token_info