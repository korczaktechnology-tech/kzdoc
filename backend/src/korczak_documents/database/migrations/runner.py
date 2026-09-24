from datetime import datetime, timezone
from uuid import uuid4

from . import MIGRATION_VERSION
from ..connection import get_database


async def _migrate_users_to_current_schema(database) -> None:
    """Normaliza usuários criados manualmente ou em versões antigas da aplicação."""
    collection = database["usuarios"]
    users = await collection.find({}).to_list(length=None)

    for user in users:
        changes = {}
        if not user.get("id"):
            changes["id"] = str(uuid4())
        if "status" not in user:
            changes["status"] = "active" if user.get("is_active", True) else "inactive"
        if "phone" not in user:
            changes["phone"] = None
        if "phone_verified" not in user:
            changes["phone_verified"] = False
        if "email_verified" not in user:
            changes["email_verified"] = False
        if "role" not in user:
            changes["role"] = "user"
        if "name" not in user:
            changes["name"] = user.get("nome") or user.get("username") or "Usuário"
        if isinstance(user.get("email"), str):
            normalized_email = user["email"].strip().casefold()
            if normalized_email != user["email"]:
                changes["email"] = normalized_email
        if "created_at" not in user:
            changes["created_at"] = datetime.now(timezone.utc)
        if "updated_at" not in user:
            changes["updated_at"] = datetime.now(timezone.utc)

        if changes:
            await collection.update_one({"_id": user["_id"]}, {"$set": changes})
        if "is_active" in user:
            await collection.update_one({"_id": user["_id"]}, {"$unset": {"is_active": ""}})


async def run_migrations() -> None:
    database = get_database()
    await _migrate_users_to_current_schema()
    await database["migrations"].update_one(
        {"version": MIGRATION_VERSION},
        {"$setOnInsert": {"version": MIGRATION_VERSION, "applied_at": datetime.now(timezone.utc)}},
        upsert=True,
    )
