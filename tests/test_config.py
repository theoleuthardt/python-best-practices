"""Tests for configuration management."""

import os
from unittest.mock import patch
from src.config import Settings

def test_default_settings():
    """Test default settings values."""
    settings = Settings()
    assert settings.app_name == "Python Best Practices"
    assert settings.debug is False
    assert settings.log_level == "INFO"


def test_env_override():
    """Test environment variable override."""
    with patch.dict(os.environ, {"DEBUG": "true", "LOG_LEVEL": "DEBUG"}):
        settings = Settings()
        assert settings.debug is True
        assert settings.log_level == "DEBUG"
