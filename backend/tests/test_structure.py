from korczak_documents.config.settings import Settings
from korczak_documents.errors import ValidationError
from korczak_documents.validators.health import validate_health_service

def test_development_settings():
    assert Settings().app_env == "development"

def test_validation_rejects_empty_service_name():
    try:
        validate_health_service("   ")
    except ValidationError:
        return
    raise AssertionError("ValidationError esperado")
