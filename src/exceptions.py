"""Custom exceptions for the application."""


class PythonBestPracticesError(Exception):
    """Base exception for all application-specific errors."""
    pass


class ConfigurationError(PythonBestPracticesError):
    """Raised when there's a configuration error."""
    pass


class ValidationError(PythonBestPracticesError):
    """Raised when data validation fails."""
    pass


class ProcessingError(PythonBestPracticesError):
    """Raised when data processing fails."""
    pass