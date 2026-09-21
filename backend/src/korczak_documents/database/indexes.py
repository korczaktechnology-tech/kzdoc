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
    """Create all indexes required by the application, idempotently."""
    for collection in COLLECTIONS:
        definitions = INDEX_DEFINITIONS[collection]
        if collection == "usuarios":
            await database[collection].create_index(
                definitions,
                unique=True,
                name="user_email_unique",
            )
        elif collection == "etiquetas":
            await database[collection].create_index(
                definitions,
                unique=True,
                name="tag_owner_name_unique",
            )
        elif collection == "sessoes":
            await database[collection].create_index(
                definitions,
                name="session_user_expires",
            )
        else:
            await database[collection].create_index(definitions)

    # IDs are application-generated UUIDs and must remain unique at the database layer.
    for collection in COLLECTIONS:
        await database[collection].create_index(
            "id",
            unique=True,
            name="id_unique",
        )

    # Session records are looked up by the SHA-256 token hash.
    await database["sessoes"].create_index(
        "token_hash",
        unique=True,
        name="session_token_hash_unique",
    )

    # Automatic expiry for sessions after their expires_at timestamp.
    await database["sessoes"].create_index(
        "expires_at",
        expireAfterSeconds=0,
        name="session_expiry",
    )

    # Full-text search used by /api/v1/search.
    await database["documentos"].create_index(
        [("name", "text"), ("description", "text"), ("document_type", "text")],
        name="document_search_text",
    )
    await database["versoes"].create_index(
        [("content", "text")],
        name="version_content_search_text",
    )

    # Audit queries by actor/resource and chronological order.
    await database["eventos"].create_index(
        [("actor_id", ASCENDING), ("created_at", DESCENDING)],
        name="audit_actor_created_at",
    )
    await database["eventos"].create_index(
        [("resource", ASCENDING), ("created_at", DESCENDING)],
        name="audit_resource_created_at",
    )
