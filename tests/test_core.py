import pytest
from src.my_stats_lib.core import mean, median, mode, variance, std
from src.my_stats_lib.exceptions import StatisticError

# mean
def test_mean_basic():
    assert mean([1, 2, 3, 4, 5]) == 3.0
    assert mean([10.0, 20.0, 30.0]) == 20.0

def test_mean_empty():
    with pytest.raises(StatisticError):
        mean([])

def test_mean_generator():
    assert mean(x for x in range(1, 6)) == 3.0

def test_mean_single_element():
    assert mean([42]) == 42.0

# median
def test_median_odd():
    assert median([7, 1, 3, 3, 2, 6]) == 3.0

def test_median_even():
    assert median([1, 3, 3, 6, 7, 8, 9]) == 6.0

def test_median_even_average():
    assert median([1, 2, 3, 4]) == 2.5

def test_median_empty():
    with pytest.raises(StatisticError):
        median([])

# mode
def test_mode():
    assert mode([1, 2, 2, 3, 4]) == 2.0
    assert mode([5, 5, 5, 1, 1]) == 5.0

def test_mode_multiple_same_frequency_returns_first():
    assert mode([1, 1, 2, 2, 3]) == 1.0   # первая встретившаяся

def test_mode_empty():
    with pytest.raises(StatisticError):
        mode([])

# variance
def test_variance_ddof0():
    # variance = 2.0
    assert pytest.approx(variance([1, 2, 3, 4, 5], ddof=0)) == 2.0


def test_variance_ddof1():
    assert pytest.approx(variance([1, 2, 3, 4, 5], ddof=1)) == 2.5

def test_variance_empty_raises():
    with pytest.raises(StatisticError):
        variance([])

def test_variance_ddof_too_big():
    with pytest.raises(StatisticError):
        variance([1, 2], ddof=3)

def test_std():
    assert pytest.approx(std([1, 2, 3, 4, 5], ddof=1)) == 1.58113883
