import os
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from korczak_documents.database.bootstrap import bootstrap_database
from korczak_documents.database.connection import get_database
from korczak_documents.main import app


@pytest.mark.integration
@pytest.mark.asyncio
async def test_api_end_to_end() -> None:
    if not os.getenv("MONGODB_URI"):
        pytest.skip("MONGODB_URI não configurado")

    await bootstrap_database()
    database = get_database()
    for collection in ("usuarios", "documentos", "versoes", "pastas", "etiquetas", "sessoes", "eventos", "notificacoes", "grupos"):
        await database[collection].delete_many({})

    client = TestClient(app)
    email = f"phase4-{uuid4().hex}@example.com"
    password = "Korczak-Fase4-2026!"

    response = client.post("/api/v1/auth/register", json={"name": "Fase 4", "email": email, "password": password})
    assert response.status_code == 201
    token = response.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}

    assert client.get("/api/v1/users/me", headers=headers).status_code == 200
    assert client.patch("/api/v1/users/me", headers=headers, json={"name": "Fase 4 Atualizada", "phone": "11999999999"}).status_code == 200

    folder = client.post("/api/v1/folders", headers=headers, json={"name": "Projetos"}).json()
    assert client.patch(f"/api/v1/folders/{folder['id']}", headers=headers, json={"name": "Projetos 2026"}).status_code == 200

    document = client.post(
        "/api/v1/documents",
        headers=headers,
        json={"name": "Documento de teste", "document_type": "txt", "folder_id": folder["id"], "content": "v1"},
    ).json()
    document_id = document["id"]
    assert document["current_version_id"]

    assert client.get(f"/api/v1/documents/{document_id}", headers=headers).status_code == 200
    assert client.get("/api/v1/documents", headers=headers).status_code == 200
    assert client.patch(f"/api/v1/documents/{document_id}", headers=headers, json={"name": "Documento atualizado"}).status_code == 200
    assert client.post(f"/api/v1/documents/{document_id}/versions", headers=headers, json={"content": "v2"}).status_code == 201
    assert client.get(f"/api/v1/documents/{document_id}/versions", headers=headers).status_code == 200

    assert client.post(f"/api/v1/documents/{document_id}/open", headers=headers).status_code == 200
    assert client.get("/api/v1/recent", headers=headers).status_code == 200
    assert client.post(f"/api/v1/documents/{document_id}/favorite", headers=headers).status_code == 200
    assert client.get("/api/v1/favorites", headers=headers).status_code == 200
    assert client.delete(f"/api/v1/documents/{document_id}/favorite", headers=headers).status_code == 200

    assert client.post("/api/v1/tags", headers=headers, json={"name": "importante"}).status_code == 201
    assert client.post(f"/api/v1/documents/{document_id}/tags/importante", headers=headers).status_code == 200
    assert client.get("/api/v1/tags", headers=headers).status_code == 200
    assert client.delete(f"/api/v1/documents/{document_id}/tags/importante", headers=headers).status_code == 200
    assert client.delete("/api/v1/tags/importante", headers=headers).status_code == 200

    group = client.post("/api/v1/groups", headers=headers, json={"name": "Equipe"}).json()
    user_id = client.get("/api/v1/users/me", headers=headers).json()["id"]
    assert client.post(f"/api/v1/groups/{group['id']}/members/{user_id}", headers=headers).status_code == 200
    assert client.delete(f"/api/v1/groups/{group['id']}/members/{user_id}", headers=headers).status_code == 200

    assert client.get(f"/api/v1/permissions/{document_id}", headers=headers).status_code == 200

    assert client.get("/api/v1/search", headers=headers, params={"q": "Documento"}).status_code == 200
    assert client.get("/api/v1/audit", headers=headers).status_code == 200
    assert client.get("/api/v1/notifications", headers=headers).status_code == 200

    await database["notificacoes"].insert_one({
        "id": str(uuid4()),
        "user_id": user_id,
        "type": "test",
        "message": "Teste",
        "read": False,
        "created_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc),
    })
    notification = client.get("/api/v1/notifications", headers=headers).json()[0]
    assert client.post(f"/api/v1/notifications/{notification['id']}/read", headers=headers).status_code == 200

    await database["usuarios"].update_one({"id": user_id}, {"$set": {"role": "admin"}})
    assert client.get("/api/v1/users", headers=headers).status_code == 200
    assert client.put(
        f"/api/v1/permissions/{document_id}",
        headers=headers,
        json={"role": "editor", "actions": ["read", "write"]},
    ).status_code == 200

    assert client.post("/api/v1/auth/recovery", json={"email": email}).status_code == 200
    assert client.post("/api/v1/auth/logout", headers=headers).status_code == 200
    assert client.get("/api/v1/users/me", headers=headers).status_code == 401

    second_email = f"phase4-other-{uuid4().hex}@example.com"
    second = client.post("/api/v1/auth/register", json={"name": "Outro", "email": second_email, "password": password})
    second_headers = {"Authorization": f"Bearer {second.json()['token']}"}
    denied = client.get(f"/api/v1/documents/{document_id}", headers=second_headers)
    assert denied.status_code == 404

    client.delete(f"/api/v1/documents/{document_id}", headers=second_headers)
    own = client.post("/api/v1/documents", headers=second_headers, json={"name": "Lixeira", "document_type": "txt"}).json()
    assert client.delete(f"/api/v1/documents/{own['id']}", headers=second_headers).status_code == 200
    assert client.get("/api/v1/trash", headers=second_headers).status_code == 200
    assert client.post(f"/api/v1/documents/{own['id']}/restore", headers=second_headers).status_code == 200
    assert client.delete(f"/api/v1/documents/{own['id']}", headers=second_headers).status_code == 200
    assert client.delete(f"/api/v1/documents/{own['id']}/permanent", headers=second_headers).status_code == 200

    await database["usuarios"].delete_many({})
    await database["documentos"].delete_many({})
    await database["versoes"].delete_many({})
    await database["pastas"].delete_many({})
    await database["etiquetas"].delete_many({})
    await database["sessoes"].delete_many({})
    await database["eventos"].delete_many({})
    await database["notificacoes"].delete_many({})
    await database["grupos"].delete_many({})
