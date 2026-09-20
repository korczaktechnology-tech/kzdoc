from collections import defaultdict, deque
from time import monotonic
from threading import Lock

from .errors import AppError

_WINDOW_SECONDS = 60.0
_MAX_ATTEMPTS = 10
_BUCKETS: dict[tuple[str, str], deque[float]] = defaultdict(deque)
_LOCK = Lock()


def enforce_rate_limit(client_key: str, action: str) -> None:
    now = monotonic()
    key = (client_key, action)
    with _LOCK:
        bucket = _BUCKETS[key]
        while bucket and now - bucket[0] >= _WINDOW_SECONDS:
            bucket.popleft()
        if len(bucket) >= _MAX_ATTEMPTS:
            raise AppError("Muitas tentativas. Tente novamente mais tarde.", "rate_limited", 429)
        bucket.append(now)


def reset_rate_limits() -> None:
    with _LOCK:
        _BUCKETS.clear()
