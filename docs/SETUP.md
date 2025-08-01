# Setup Guide

This guide walks you through setting up the Python Best Practices project from scratch.

## Prerequisites

- Python 3.9 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## Quick Start

### 1. Install uv

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with brew
brew install uv

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone and Setup Project

```bash
# Clone the repository
git clone <your-repo-url>
cd python-best-practices

# Create virtual environment
uv venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install project in development mode
uv pip install -e ".[dev]"
```

### 3. Verify Installation

```bash
# Run tests
pytest

# Check code quality
ruff check src/ tests/
mypy src/

# Format code
black src/ tests/

# Run CLI
python -m python_best_practices.cli --help
```

## Project Structure

```
python-best-practices/
├── src/
│   ├── __init__.py          # Package initialization
│   ├── cli.py               # Command line interface
│   ├── config.py            # Configuration management
│   ├── logger.py            # Logging setup
│   ├── exceptions.py        # Custom exceptions
│   └── utils.py             # Utility functions
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest configuration
│   ├── test_cli.py              # CLI tests
│   ├── test_config.py           # Configuration tests
│   └── test_utils.py            # Utility tests
├── docs/
│   └── SETUP.md                 # This file to guide you
├── pyproject.toml               # Project configuration
├── .env.example                 # Environment variables example
├── .gitignore                   # Git ignore patterns
└── README.md                    # Project documentation
```

## Development Workflow

### Setting up Development Environment

1. **Copy environment file**:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

#### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_cli.py

# Run tests with specific markers
pytest -m "not slow"
```

#### Code Quality Checks

```bash
# Check code style and lint
ruff check src/ tests/

# Auto-fix issues
ruff check --fix src/ tests/

# Format code
black src/ tests/

# Type checking
mypy src/
```

#### Using Task Automation

**With invoke** (recommended):
```bash
# Run all checks
invoke check

# Individual tasks
invoke test
invoke lint
invoke format
invoke clean
```

**With Make**:
```bash
# Run all checks
make check

# Individual tasks
make test
make lint
make format
make clean
```

### Configuration Management

The project uses **Pydantic Settings** for configuration:

- **Environment Variables**: Define in `.env` file or system environment
- **Type Safety**: All settings are type-checked
- **Validation**: Automatic validation of configuration values

Example usage:
```python
from src.config import settings

print(settings.app_name)  # "Python Best Practices"
print(settings.debug)     # False (default)
```