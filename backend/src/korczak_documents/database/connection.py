from functools import lru_cache

from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from ..config.settings import Settings, get_settings


@lru_cache
def get_client() -> AsyncMongoClient:
    settings = get_settings()
    return AsyncMongoClient(settings.mongodb_uri, serverSelectionTimeoutMS=settings.mongodb_server_selection_timeout_ms)


def get_database(settings: Settings | None = None) -> AsyncDatabase:
    current = settings or get_settings()
    return get_client()[current.mongodb_database]
