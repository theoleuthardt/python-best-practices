"""Tests for CLI functionality."""

from typer.testing import CliRunner
from src.cli import app

runner = CliRunner()


def test_hello_command():
    """Test the hello command."""
    result = runner.invoke(app, ["hello", "World"])
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout


def test_info_command():
    """Test the info command."""
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "Python Best Practices" in result.stdout
    assert "pytest" in result.stdout
