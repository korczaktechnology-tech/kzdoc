from datetime import datetime, timezone
from uuid import uuid4

from ..database.connection import get_database


def now() -> datetime:
    return datetime.now(timezone.utc)


def _redact_payload(payload: dict) -> dict:
    sensitive = ("password", "token", "secret", "authorization", "cookie", "api_key", "content")
    return {k: ("[REDACTED]" if any(term in k.casefold() for term in sensitive) else v) for k, v in payload.items()}


async def find_user_by_email(email: str):
    return await get_database()["usuarios"].find_one({"email": email.lower().strip()})


async def find_user(user_id: str):
    return await get_database()["usuarios"].find_one({"id": user_id})


async def create_user(data: dict):
    document = {
        "id": str(uuid4()),
        "name": data["name"].strip(),
        "email": data["email"].lower().strip(),
        "phone": data.get("phone"),
        "password_hash": data["password_hash"],
        "email_verified": False,
        "phone_verified": False,
        "role": data.get("role", "user"),
        "status": data.get("status", "active"),
        "created_at": now(),
        "updated_at": now(),
    }
    await get_database()["usuarios"].insert_one(document)
    return document


async def update_user(user_id: str, changes: dict):
    changes["updated_at"] = now()
    await get_database()["usuarios"].update_one({"id": user_id}, {"$set": changes})
    return await find_user(user_id)


async def create_document(owner_id: str, data: dict):
    document = {
        "id": str(uuid4()), "owner_id": owner_id, "name": data["name"].strip(),
        "document_type": data["document_type"].strip(), "folder_id": data.get("folder_id"),
        "current_version_id": None, "status": "active", "favorite_user_ids": [],
        "created_at": now(), "updated_at": now(),
    }
    await get_database()["documentos"].insert_one(document)
    return document


async def get_document(document_id: str):
    return await get_database()["documentos"].find_one({"id": document_id})


async def list_documents(owner_id: str, query: dict, skip: int, limit: int):
    collection = get_database()["documentos"]
    filters = {"owner_id": owner_id, **query}
    total = await collection.count_documents(filters)
    cursor = collection.find(filters).sort("updated_at", -1).skip(skip).limit(limit)
    return await cursor.to_list(length=limit), total


async def update_document(document_id: str, changes: dict):
    changes["updated_at"] = now()
    await get_database()["documentos"].update_one({"id": document_id}, {"$set": changes})
    return await get_document(document_id)


async def create_version(document_id: str, author_id: str, content: str | None, number: int):
    version = {"id": str(uuid4()), "document_id": document_id, "version_number": number, "author_id": author_id, "content": content, "created_at": now()}
    await get_database()["versoes"].insert_one(version)
    await update_document(document_id, {"current_version_id": version["id"]})
    return version


async def get_version(version_id: str):
    return await get_database()["versoes"].find_one({"id": version_id})


async def list_versions(document_id: str):
    return await get_database()["versoes"].find({"document_id": document_id}).sort("version_number", -1).to_list(length=500)


async def create_folder(owner_id: str, data: dict):
    folder = {"id": str(uuid4()), "owner_id": owner_id, "parent_id": data.get("parent_id"), "name": data["name"].strip(), "created_at": now(), "updated_at": now()}
    await get_database()["pastas"].insert_one(folder)
    return folder


async def list_folders(owner_id: str):
    return await get_database()["pastas"].find({"owner_id": owner_id}).sort("name", 1).to_list(length=1000)


async def get_folder(folder_id: str):
    return await get_database()["pastas"].find_one({"id": folder_id})


async def update_folder(folder_id: str, changes: dict):
    changes["updated_at"] = now()
    await get_database()["pastas"].update_one({"id": folder_id}, {"$set": changes})
    return await get_folder(folder_id)


async def delete_folder(folder_id: str):
    await get_database()["pastas"].delete_one({"id": folder_id})


async def log_event(user_id: str | None, event_type: str, payload: dict):
    await get_database()["eventos"].insert_one({"id": str(uuid4()), "user_id": user_id, "type": event_type, "payload": _redact_payload(payload), "created_at": now()})


async def list_events(user_id: str, filters: dict, skip: int, limit: int):
    collection = get_database()["eventos"]
    query = {"user_id": user_id, **filters}
    total = await collection.count_documents(query)
    items = await collection.find(query).sort("created_at", -1).skip(skip).limit(limit).to_list(length=limit)
    return items, total
