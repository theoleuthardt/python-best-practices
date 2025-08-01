"""Logging configuration following best practices."""

import logging
from pathlib import Path
from typing import Optional

from rich.logging import RichHandler

from .config import settings


def setup_logging(
        level: Optional[str] = None,
        log_file: Optional[Path] = None,
) -> logging.Logger:
    """Set up logging with rich formatting and optional file output.

    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional file path for log output

    Returns:
        Configured logger instance
    """
    # Get log level from settings if not provided
    log_level = level or settings.log_level

    # Create logger
    logger = logging.getLogger("python_best_practices")
    logger.setLevel(getattr(logging, log_level.upper()))

    # Clear existing handlers
    logger.handlers.clear()

    # Console handler with rich formatting
    console_handler = RichHandler(
        rich_tracebacks=True,
        markup=True,
        show_path=settings.debug,
    )
    console_handler.setLevel(getattr(logging, log_level.upper()))

    # Format
    formatter = logging.Formatter(
        fmt="%(message)s",
        datefmt="[%X]",
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Optional file handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger


# Default logger instance
logger = setup_logging()