from .connection import get_database
from .indexes import ensure_indexes
from .migrations.runner import run_migrations
from .seed import seed_initial_data


async def bootstrap_database() -> None:
    database = get_database()
    await database.command({"ping": 1})
    await run_migrations()
    await ensure_indexes(database)
    await seed_initial_data()
