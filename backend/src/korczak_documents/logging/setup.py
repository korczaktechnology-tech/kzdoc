import logging
from ..config.settings import Settings
_CONFIGURED = False

def configure_logging(settings: Settings) -> None:
    global _CONFIGURED
    if _CONFIGURED: return
    level = getattr(logging, settings.log_level.upper(), logging.INFO)
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    _CONFIGURED = True

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
