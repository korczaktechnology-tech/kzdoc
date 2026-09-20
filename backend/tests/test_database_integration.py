import os
from datetime import datetime, timezone

import pytest

from korczak_documents.database.bootstrap import bootstrap_database
from korczak_documents.database.connection import get_database
from korczak_documents.database.seed import seed_initial_data


@pytest.mark.integration
@pytest.mark.asyncio
async def test_mongodb_bootstrap_and_recovery_round_trip() -> None:
    if not os.getenv("MONGODB_URI"):
        pytest.skip("MONGODB_URI não configurado")

    await bootstrap_database()
    await seed_initial_data()

    database = get_database()
    collection = database["eventos"]
    marker = {"type": "test.recovery", "created_at": datetime.now(timezone.utc)}

    await collection.insert_one(marker)
    saved = await collection.find_one({"type": "test.recovery"})
    assert saved is not None

    await collection.delete_one({"_id": saved["_id"]})
    assert await collection.find_one({"_id": saved["_id"]}) is None

    await collection.insert_one(saved)
    restored = await collection.find_one({"_id": saved["_id"]})
    assert restored is not None

    await collection.delete_one({"_id": saved["_id"]})
