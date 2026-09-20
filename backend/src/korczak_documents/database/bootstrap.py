from .connection import get_database
from .indexes import ensure_indexes


async def bootstrap_database() -> None:
    database = get_database()
    await database.command({"ping": 1})
    await ensure_indexes(database)
