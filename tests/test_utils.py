import pytest
import warnings
from src.my_stats_lib.utils import ensure_list, is_numeric

def test_is_numeric_numbers():
    assert is_numeric(5) is True
    assert is_numeric(5.0) is True
    assert is_numeric(-3) is True
    assert is_numeric(0) is True

def test_is_numeric_not_numbers():
    assert is_numeric("5") is False
    assert is_numeric([1, 2]) is False
    assert is_numeric(None) is False
    assert is_numeric(True) is False
    assert is_numeric(False) is False
    assert is_numeric(1+2j) is False

def test_is_numeric_edge_cases():
    assert is_numeric(0) is True
    assert is_numeric(0.0) is True

def test_ensure_list_list_and_tuple():
    assert ensure_list([1, 2, 3]) == [1, 2, 3]
    assert ensure_list((1, 2, 3)) == [1, 2, 3]


def test_ensure_list_generator():
    gen = (x for x in range(5))

    with pytest.warns(UserWarning, match="Преобразование генератора в список"):
        result = ensure_list(gen)

    assert result == [0, 1, 2, 3, 4]

def test_ensure_list_string():
    assert ensure_list("abc") == ['a', 'b', 'c']