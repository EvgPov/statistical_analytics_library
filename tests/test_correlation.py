import pytest
from src.my_stats_lib.correlation import covariance, pearson_correlation

# covariance
def test_covariance_basic():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    assert pytest.approx(covariance(x, y)) == 5.0


def test_covariance_ddof0():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    assert pytest.approx(covariance(x, y, ddof=0)) == 4.0

def test_covariance_different_length_raises():
    x = [1, 2, 3]
    y = [1, 2]
    with pytest.raises(ValueError):
        covariance(x, y)

def test_pearson_empty_raises():
    with pytest.raises(ValueError):
        covariance([], [])

# pearson_correlation
def test_pearson_perfect_positive():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    assert pytest.approx(pearson_correlation(x, y)) == 1.0

def test_pearson_perfect_negative():
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]
    assert pytest.approx(pearson_correlation(x, y)) == -1.0

def test_pearson_no_correlation():
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 2, 1]
    assert pytest.approx(pearson_correlation(x, y), abs=0.01) == -1.0

def test_pearson_zero_std_raises():
    x = [1, 1, 1, 1]
    y = [2, 3, 4, 5]
    with pytest.raises(ValueError):
        pearson_correlation(x, y)

def test_pearson_different_length_raises():
    with pytest.raises(ValueError):
        pearson_correlation([1, 2], [1, 2, 3])