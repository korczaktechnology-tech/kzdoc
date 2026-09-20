from .settings import Settings

settings = Settings(
    app_env="production",
    api_host="0.0.0.0",
    api_port=8000,
    log_level="INFO",
)
