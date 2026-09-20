from ..errors import ValidationError


def require_reference(value: str | None, field: str) -> str:
    if not value or not value.strip():
        raise ValidationError(f"{field} é obrigatório")
    return value.strip()


def ensure_document_owner(owner_id: str, document_owner_id: str) -> None:
    if owner_id != document_owner_id:
        raise ValidationError("Documento não pertence ao usuário informado")


def ensure_version_number(value: int) -> int:
    if value < 1:
        raise ValidationError("A versão deve ser maior ou igual a 1")
    return value


def ensure_folder_parent(owner_id: str, parent_owner_id: str | None) -> None:
    if parent_owner_id is not None and owner_id != parent_owner_id:
        raise ValidationError("A pasta pai deve pertencer ao mesmo usuário")
