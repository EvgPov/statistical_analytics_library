import pytest
import time
from src.my_stats_lib.decorators import timer, logger, validate_numeric, memoize
from src.my_stats_lib.core import mean

def test_timer_decorator(capsys):
    @timer
    def slow_function():
        time.sleep(0.1)
        return 42

    result = slow_function()
    assert result == 42

    captured = capsys.readouterr()
    assert "slow_function выполнена за" in captured.out

def test_logger_decorator(capsys):
    @logger
    def add(a, b):
        return a + b

    result = add(3, 5)
    assert result == 8

    captured = capsys.readouterr()
    assert "Вызов add" in captured.out
    assert "add вернула: 8" in captured.out

def test_validate_numeric_passes():
    @validate_numeric
    def compute_mean(data):
        return mean(data)

    assert compute_mean([1, 2, 3]) == 2.0


def test_validate_numeric_raises():
    @validate_numeric
    def compute_mean(data):
        return mean(data)

    with pytest.raises(TypeError):
        compute_mean([1, 2, "3", 4])

def test_memoize():
    call_count = 0

    @memoize()
    def expensive_function(x):
        nonlocal call_count
        call_count += 1
        return x * x

    assert expensive_function(5) == 25
    assert expensive_function(5) == 25
    assert expensive_function(6) == 36
    assert call_count == 2


def test_memoize_with_maxsize():
    @memoize(maxsize=2)
    def func(x):
        return x * 10

    assert func(1) == 10
    assert func(2) == 20
    assert func(3) == 30
    assert func(2) == 20