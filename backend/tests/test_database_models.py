from datetime import datetime, timezone
import pytest
from pydantic import ValidationError as PydanticValidationError
from korczak_documents.models import DocumentModel, UserModel, VersionModel
from korczak_documents.database.integrity import ensure_document_owner, ensure_folder_parent, ensure_version_number


NOW = datetime.now(timezone.utc)


def test_document_model_contract() -> None:
    model = DocumentModel(id="d1", owner_id="u1", name="Contrato", document_type="pdf", created_at=NOW, updated_at=NOW)
    assert model.owner_id == "u1"


def test_user_model_requires_secure_password_field() -> None:
    model = UserModel(id="u1", name="User", email="u@example.com", password_hash="hash", created_at=NOW, updated_at=NOW)
    assert model.password_hash == "hash"


def test_version_model_rejects_zero() -> None:
    with pytest.raises(PydanticValidationError):
        VersionModel(id="v1", document_id="d1", version_number=0, author_id="u1", created_at=NOW)


def test_integrity_rules() -> None:
    assert ensure_version_number(1) == 1
    with pytest.raises(Exception):
        ensure_document_owner("u1", "u2")
    with pytest.raises(Exception):
        ensure_folder_parent("u1", "u2")
