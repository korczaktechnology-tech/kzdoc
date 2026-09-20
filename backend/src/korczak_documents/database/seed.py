from datetime import datetime, timezone

from .collections import COLLECTIONS
from .connection import get_database


async def seed_initial_data() -> None:
    """Cria somente os marcadores mínimos de infraestrutura, sem dados de usuários."""
    database = get_database()
    now = datetime.now(timezone.utc)
    await database["eventos"].update_one(
        {"type": "system.bootstrap"},
        {"$setOnInsert": {"type": "system.bootstrap", "created_at": now, "collections": list(COLLECTIONS)}},
        upsert=True,
    )
