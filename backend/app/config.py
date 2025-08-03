from typing import Annotated

from fastapi import Depends
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Application settings."""

    # MAL settings
    mal_client_id: str = "your-mal-client-id"
    mal_client_secret: str = "your-mal-client-secret"
    mal_refresh_token: str = "your-mal-refresh-token"
    mal_access_token: str = "your-mal-access-token"

    # Plex settings
    plex_url: str = "http://your.plex.server:32400"
    plex_token: str = "your-plex-token"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


app_settings = AppSettings()

AppConfig = Annotated[AppSettings, Depends(lambda: app_settings)]
