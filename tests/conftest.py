"""Pytest configuration and fixtures."""

import pytest
from src.config import Settings

@pytest.fixture
def temp_dir(tmp_path):
    """Provide a temporary directory for tests."""
    return tmp_path


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "hobbies": ["reading", "coding"],
    }


@pytest.fixture
def mock_settings():
    """Provide mock settings for tests."""
    return Settings(
        app_name="Test App",
        debug=True,
        log_level="DEBUG",
        api_key="test_api_key",
        api_url="https://api.test.com"
    )