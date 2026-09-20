from .collections import COLLECTIONS
from .connection import get_database
from .indexes import ensure_indexes

__all__ = ["COLLECTIONS", "get_database", "ensure_indexes"]
