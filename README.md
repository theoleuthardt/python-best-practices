# 🐍 Python Best Practices

This repository documents my learning progress on Python best practices – including clean code architecture, 
modern tools, dependency management, tests, typing, formatting, and much more.

---

## 🚀 Project Goal

The goal of this repo is to build a solid, future-proof Python setup through practical examples and notes 
that excels both in everyday use and in professional software development.

---

## 🧪 Starting the Project (with `uv`)

[`uv`](https://github.com/astral-sh/uv) is an ultra-fast Python package manager that replaces `pip`, `pip-tools`, `virtualenv`
and more – all in a single tool.

### 🔧 Installing `uv`

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

Or via brew (macOS/Linux):
```zsh
brew install astral-sh/uv/uv
```
uv requires no root privileges and installs locally in the user context.

### 📦 Setting Up the Project
#### 1. Create virtual environment with uv
```bash
uv venv
source .venv/bin/activate 
```

#### 2. Install dependencies
```bash
uv pip install -r requirements.txt
```
Or for initial setup:
```bash
uv pip install <package-name>
uv pip freeze > requirements.txt
```

## 📁 Structure (ideally)

```
python-best-practices/
├── src/
│   └── ...
├── tests/
│   └── ...
├── requirements.txt
└── README.md
```

## 📚 Included Best Practices

### 🔧 Development Environment
✅ Using `uv` for fast, clean environments  
✅ Virtual environments with `uv`  
✅ Dependency management with `pip-tools`  
✅ Environment configuration with `.env` files  

### 📝 Code Quality
✅ Type hints and default-value parameters  
✅ Code formatting with `black` and `ruff`  
✅ Linting with `pylint` or `flake8`  
✅ Import sorting with `isort`  
✅ Docstrings following PEP 257  

### 🧪 Testing & Quality Assurance
✅ Tests with `pytest`  
✅ Test coverage with `coverage.py`  
✅ Property-based testing with `hypothesis`  
✅ Mocking with `unittest.mock` or `pytest-mock`  

### 🏗️ Project Structure & Architecture
✅ Clean project structure (`src/` layout)  
✅ Configuration management  
✅ Logging best practices  
✅ Error handling and custom exceptions  

### 🚀 CLI & Automation
✅ Simple CLI tools with `typer`  
✅ Task automation with `invoke` or `make`  
✅ Pre-commit hooks for code quality  

### 📦 Distribution & Deployment
✅ Package configuration with `pyproject.toml`  
✅ Semantic versioning  
✅ Documentation with `mkdocs` or `sphinx`  

---

## 🛠️ Additional Tools & Commands

### Code Quality Checks
```bash
# Format code
uv run black src/ tests/
uv run ruff check src/ tests/

# Type checking
uv run mypy src/

# Run tests with coverage
uv run pytest --cov=src tests/
```

### Pre-commit Setup
```bash
# Install pre-commit
uv pip install pre-commit

# Install hooks
pre-commit install

# Run on all files
pre-commit run --all-files
```

---

## 📖 Resources & Learning Materials

- [Real Python](https://realpython.com/) - Comprehensive Python tutorials
- [Python Enhancement Proposals (PEPs)](https://peps.python.org/) - Official Python standards
- [Clean Code in Python](https://github.com/zedr/clean-code-python) - Clean code principles for Python
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/) - Best practices guide
- [Python Testing 101](https://python-testing-101.readthedocs.io/) - Testing guide