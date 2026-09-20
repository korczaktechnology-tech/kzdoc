from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Korczak Documents API"
    app_env: str = "development"
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    log_level: str = "INFO"
    frontend_url: str = "http://localhost:5173"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore", case_sensitive=False)
    @property
    def is_production(self) -> bool:
        return self.app_env.lower() == "production"

@lru_cache
def get_settings() -> Settings:
    return Settings()
