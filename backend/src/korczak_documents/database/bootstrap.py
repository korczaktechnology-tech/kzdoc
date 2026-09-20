from .connection import get_database
from .indexes import ensure_indexes
from .migrations.runner import run_migrations
from .seed import seed_initial_data
from .collections import COLLECTIONS


async def bootstrap_database() -> None:
    database = get_database()
    await database.command({"ping": 1})
    await run_migrations()

    existing = set(await database.list_collection_names())
    for collection in COLLECTIONS:
        if collection not in existing:
            await database.create_collection(collection)

    await ensure_indexes(database)
    await seed_initial_data()
