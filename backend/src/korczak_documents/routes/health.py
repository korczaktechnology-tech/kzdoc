from fastapi import APIRouter
from ..models.health import HealthResponse
from ..services.health import HealthService
from ..validators.health import validate_health_service
router = APIRouter()
_service = HealthService()
@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    service = validate_health_service("korczak-documents-api")
    return HealthResponse(status=_service.check(), service=service)
