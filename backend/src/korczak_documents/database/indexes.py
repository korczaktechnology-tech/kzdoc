from pymongo import ASCENDING, DESCENDING

from .collections import COLLECTIONS

INDEX_DEFINITIONS = {
    "usuarios": [("email", ASCENDING)],
    "documentos": [("owner_id", ASCENDING), ("updated_at", DESCENDING)],
    "versoes": [("document_id", ASCENDING), ("version_number", DESCENDING)],
    "pastas": [("owner_id", ASCENDING), ("parent_id", ASCENDING)],
    "etiquetas": [("owner_id", ASCENDING), ("name", ASCENDING)],
    "sessoes": [("user_id", ASCENDING), ("expires_at", ASCENDING)],
    "eventos": [("user_id", ASCENDING), ("created_at", DESCENDING)],
    "notificacoes": [("user_id", ASCENDING), ("read", ASCENDING), ("created_at", DESCENDING)],
    "grupos": [("owner_id", ASCENDING), ("name", ASCENDING)],
}


async def ensure_indexes(database) -> None:
    for collection in COLLECTIONS:
        await database[collection].create_index(INDEX_DEFINITIONS[collection])
