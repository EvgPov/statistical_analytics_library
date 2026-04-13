import time
import functools
from functools import wraps
from .utils import is_numeric


def timer(func):
    """Выводит время выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} выполнена за {end - start:.4f} секунд")
        return result
    return wrapper


def logger(func):
    """Логирует вызов функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} вернула: {result}")
        return result
    return wrapper


def validate_numeric(func):
    """Проверяет, что все аргументы-коллекции содержат только числа."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (list, tuple)):
                for item in arg:
                    if not is_numeric(item):
                        raise TypeError(f"Ожидалось число, получено {type(item).__name__}")
        return func(*args, **kwargs)
    return wrapper


def memoize(maxsize=None):
    """Кэширует результаты функции (с поддержкой maxsize)."""
    def decorator(func):
        @functools.lru_cache(maxsize=maxsize)
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator