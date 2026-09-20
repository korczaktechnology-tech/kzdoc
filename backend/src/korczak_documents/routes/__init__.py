from .api import router as api_router
from .health import router as health_router

router = api_router
router.include_router(health_router)
__all__ = ["router"]
