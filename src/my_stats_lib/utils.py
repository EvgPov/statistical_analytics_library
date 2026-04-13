import warnings
from collections.abc import Iterable

def ensure_list(iterable):
    if isinstance(iterable, (list, tuple)):
        return list(iterable)

    if isinstance(iterable, Iterable) and not isinstance(iterable, (str, bytes)):
        warnings.warn(
            "Преобразование генератора в список. Данные будут загружены в память.",
            UserWarning,
            stacklevel=2
        )
    return list(iterable)
def is_numeric(value):
    if isinstance(value, bool):
        return False
    return isinstance(value, (int, float))