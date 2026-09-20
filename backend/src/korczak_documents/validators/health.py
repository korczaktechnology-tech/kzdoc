from ..errors import ValidationError
def validate_health_service(service_name: str) -> str:
    value = service_name.strip()
    if not value: raise ValidationError("O nome do serviço não pode ser vazio.")
    return value
