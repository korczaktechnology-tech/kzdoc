import os
from datetime import datetime, timezone
import pytest
from korczak_documents.database.bootstrap import bootstrap_database
from korczak_documents.database.connection import get_database


@pytest.mark.integration
@pytest.mark.asyncio
async def test_mongodb_bootstrap_indexes_seed_and_recovery_round_trip() -> None:
    if not os.getenv("MONGODB_URI"):
        pytest.skip("MONGODB_URI não configurado")
    await bootstrap_database()
    database = get_database()
    assert database.name == "KZDocs"
    collections = await database.list_collection_names()
    assert "eventos" in collections
    assert "migrations" in collections
    indexes = await database["documentos"].index_information()
    assert any("owner_id" in str(index.get("key")) for index in indexes.values())
    marker = {"type": "test.recovery", "created_at": datetime.now(timezone.utc)}
    await database["eventos"].insert_one(marker)
    saved = await database["eventos"].find_one({"type": "test.recovery"})
    assert saved is not None
    await database["eventos"].delete_one({"_id": saved["_id"]})
    assert await database["eventos"].find_one({"_id": saved["_id"]}) is None
    await database["eventos"].insert_one(saved)
    assert await database["eventos"].find_one({"_id": saved["_id"]}) is not None
    await database["eventos"].delete_one({"_id": saved["_id"]})
