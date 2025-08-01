"""Utility functions and helpers."""

import functools
import time
from typing import Any, Callable, TypeVar
from .logger import logger

F = TypeVar('F', bound=Callable[..., Any])


def timer(func: F) -> F:
    """Decorator to time function execution."""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result

    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable[[F], F]:
    """Decorator to retry function execution on failure."""

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        logger.warning(
                            f"Attempt {attempt + 1} failed for {func.__name__}: {e}. "
                            f"Retrying in {delay} seconds..."
                        )
                        time.sleep(delay)
                    else:
                        logger.error(f"All {max_attempts} attempts failed for {func.__name__}")

            raise last_exception

        return wrapper

    return decorator
