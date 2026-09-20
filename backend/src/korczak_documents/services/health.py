from ..repositories.health import HealthRepository
class HealthService:
    def __init__(self, repository: HealthRepository | None = None): self.repository = repository or HealthRepository()
    def check(self) -> str: return self.repository.status()
