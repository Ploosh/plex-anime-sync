# plex-anime-sync

Keeps a Plex anime library in sync with MyAnimeList and AniList.

Personal project. Built to scratch my own itch (manually updating watch progress across three places was annoying) and to play with a clean full-stack setup: a Python FastAPI backend, a TypeScript frontend, and Docker Compose for local dev.

## What it does

- Reads the current state of an anime library and watch progress from a Plex server.
- Reconciles that state against MyAnimeList and AniList accounts.
- Pushes updates so all three stay consistent (episodes watched, list status, scores).

## Stack

- **Backend:** Python + FastAPI, managed with `uv`
- **Frontend:** TypeScript, Node.js dev server
- **Infra:** Docker Compose for local development
- **External APIs:** Plex, MyAnimeList, AniList

## Running locally

Requires Docker and Docker Compose.

1. Copy `backend/.env.example` to `backend/.env` and fill in Plex and MyAnimeList credentials.
2. From the repo root:

   ```bash
   docker compose up --build
   ```

3. Backend runs on `http://localhost:8000`, frontend on `http://localhost:3000`.

## Repository layout

```
backend/            FastAPI service (sync logic, API clients, endpoints)
frontend/           TypeScript web UI
docker-compose.yml  Local dev orchestration
```

## Status

Working for my own use. Not packaged for general distribution, so some configuration is hardcoded for a single-user setup. Treat it as a reference project rather than a turnkey tool.

## License

MIT.
