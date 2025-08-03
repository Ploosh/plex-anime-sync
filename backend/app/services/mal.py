import httpx
import os
import requests

def exchange_code_for_token(code: str):
    data = {
        "grant_type": "authorization_code",
        "client_id": MAL_CLIENT_ID,
        "client_secret": MAL_CLIENT_SECRET,
        "code": code,
        "redirect_uri": MAL_REDIRECT_URI
    }
    response = requests.post("https://myanimelist.net/v1/oauth2/token", data=data)
    return response.json()

def update_mal(anime):
    headers = {"Authorization": f"Bearer {os.getenv('MAL_ACCESS_TOKEN')}"}
    search_url = f"https://api.myanimelist.net/v2/anime?q={anime['title']}&limit=1"
    search_res = httpx.get(search_url, headers=headers).json()

    if "data" not in search_res:
        return {"title": anime["title"], "status": "not_found"}

    anime_id = search_res["data"][0]["node"]["id"]
    update_url = f"https://api.myanimelist.net/v2/anime/{anime_id}/my_list_status"
    payload = {
        "status": "watching",
        "num_watched_episodes": anime["episodes_watched"],
        "score": anime["rating"]
    }
    httpx.patch(update_url, headers=headers, data=payload)
    return {"title": anime["title"], "status": "updated"}
