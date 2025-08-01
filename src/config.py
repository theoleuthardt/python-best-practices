"""Configuration management using Pydantic and environment variables."""

from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    app_name: str = Field(default="Python Best Practices", env="APP_NAME")
    debug: bool = Field(default=False, env="DEBUG")
    log_level: str = Field(default="INFO", env="LOG_LEVEL")

    project_root: Path = Field(default_factory=lambda: Path(__file__).parent.parent.parent)
    data_dir: Optional[Path] = Field(default=None, env="DATA_DIR")

    api_key: Optional[str] = Field(default=None, env="API_KEY")
    api_url: str = Field(default="https://api.example.com", env="API_URL")

    class Config:
        """Pydantic config."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()