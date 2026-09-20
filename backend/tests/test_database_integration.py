import os
from datetime import datetime, timezone
from pathlib import Path

import pytest

from korczak_documents.database.backup import create_backup, restore_backup
from korczak_documents.database.bootstrap import bootstrap_database
from korczak_documents.database.collections import COLLECTIONS
from korczak_documents.database.connection import get_database


@pytest.mark.integration
@pytest.mark.asyncio
async def test_mongodb_bootstrap_indexes_seed_and_recovery_round_trip(tmp_path: Path) -> None:
    if not os.getenv("MONGODB_URI"):
        pytest.skip("MONGODB_URI não configurado")

    await bootstrap_database()
    database = get_database()

    assert database.name == "KZDocs"
    collections = set(await database.list_collection_names())
    assert set(COLLECTIONS).issubset(collections)
    assert "migrations" in collections

    indexes = await database["documentos"].index_information()
    assert any("owner_id" in str(index.get("key")) for index in indexes.values())

    marker = {
        "type": "test.recovery",
        "created_at": datetime.now(timezone.utc),
        "payload": "backup-round-trip",
    }
    await database["eventos"].delete_many({"type": "test.recovery"})
    await database["eventos"].insert_one(marker)
    saved = await database["eventos"].find_one({"type": "test.recovery"})
    assert saved is not None

    archive = create_backup(os.environ["MONGODB_URI"], database.name, str(tmp_path / "backup"))
    assert Path(archive).is_file()
    assert Path(archive).stat().st_size > 0

    await database["eventos"].delete_many({"type": "test.recovery"})
    assert await database["eventos"].find_one({"type": "test.recovery"}) is None

    restore_backup(os.environ["MONGODB_URI"], database.name, archive)
    restored = await database["eventos"].find_one({"type": "test.recovery"})
    assert restored is not None
    assert restored["payload"] == "backup-round-trip"

    await database["eventos"].delete_many({"type": "test.recovery"})
