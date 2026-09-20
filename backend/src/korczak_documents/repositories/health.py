class HealthRepository:
    """Abstração inicial para dependências de persistência da API."""

    def status(self) -> str:
        return "ok"
