"""Application settings, loaded from environment variables.

Every configurable value lives here. Nothing is hard-coded elsewhere,
and no secret is ever committed - see .env.example for the shape.
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --- Service ---
    app_name: str = "vow-agent"
    environment: Literal["local", "sandbox", "staging", "production"] = "local"
    debug: bool = False
    log_level: str = "INFO"

    # --- API ---
    api_prefix: str = "/api/v1"
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    # --- Database (PLT-03 checkpointer, KNW registry) ---
    database_url: str = "postgresql+asyncpg://vowagent:vowagent@localhost:5432/vowagent"
    # --- Checkpointer ---
    # True  = in-memory (no Postgres needed; state lost on restart)
    # False = Postgres (state survives restarts; needs database_url)
    use_memory_checkpointer: bool = True

    # --- VOW platform API (PLT-04 tool wrappers) ---
    vow_api_base_url: str = "https://staging.vowmade.dev/api"
    vow_api_timeout_seconds: float = 10.0
    vow_api_max_retries: int = 3

    # --- LLM ---
    anthropic_api_key: str = ""
    llm_model: str = "claude-sonnet-4-6"

    @property
    def is_production(self) -> bool:
        return self.environment == "production"


@lru_cache
def get_settings() -> Settings:
    """Cached so settings are parsed once per process."""
    return Settings()