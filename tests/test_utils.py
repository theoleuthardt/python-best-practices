"""Tests for utility functions."""

import time
import pytest
from unittest.mock import patch
from src.utils import timer, retry
from src.exceptions import ProcessingError


def test_timer_decorator():
    """Test the timer decorator."""

    @timer
    def slow_function():
        time.sleep(0.1)
        return "done"

    with patch('python_best_practices.utils.logger') as mock_logger:
        result = slow_function()
        assert result == "done"
        mock_logger.info.assert_called_once()
        assert "took" in mock_logger.info.call_args[0][0]


def test_retry_decorator_success():
    """Test retry decorator with successful function."""
    call_count = 0

    @retry(max_attempts=3)
    def sometimes_fails():
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise ProcessingError("Temporary failure")
        return "success"

    result = sometimes_fails()
    assert result == "success"
    assert call_count == 2


def test_retry_decorator_failure():
    """Test retry decorator with always failing function."""

    @retry(max_attempts=2, delay=0.01)
    def always_fails():
        raise ProcessingError("Always fails")

    with pytest.raises(ProcessingError):
        always_fails()