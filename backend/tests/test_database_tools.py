from pathlib import Path
from unittest.mock import patch
from korczak_documents.database.backup import create_backup, restore_backup


def test_backup_invokes_mongodump(tmp_path: Path) -> None:
    with patch("subprocess.run") as run:
        run.return_value.returncode = 0
        result = create_backup("mongodb://localhost:27017", "KZDocs", str(tmp_path))
        assert result == str(tmp_path)
        run.assert_called_once()
        assert run.call_args.args[0][0] == "mongodump"


def test_restore_invokes_mongorestore() -> None:
    with patch("subprocess.run") as run:
        run.return_value.returncode = 0
        restore_backup("mongodb://localhost:27017", "KZDocs", "/tmp/backup")
        assert run.call_args.args[0][0] == "mongorestore"
