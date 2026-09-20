from fastapi import FastAPI
from .config.settings import get_settings
from .errors import register_exception_handlers
from .logging import configure_logging, get_logger
from .routes import router

settings = get_settings()
configure_logging(settings)
logger = get_logger(__name__)

app = FastAPI(title=settings.app_name, version="0.1.0")
register_exception_handlers(app)
app.include_router(router, prefix="/api/v1")

@app.get("/health", include_in_schema=False)
def root_health() -> dict[str, str]:
    logger.debug("Health check executado")
    return {"status": "ok", "service": "korczak-documents-api"}
