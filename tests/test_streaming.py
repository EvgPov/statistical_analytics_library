import pytest
from src.my_stats_lib.streaming import (
    read_numbers_from_file,
    sliding_window,
    streaming_mean,
    streaming_variance,
    streaming_pearson
)


# ==================== sliding_window ====================

def test_sliding_window_basic():
    data = [1, 2, 3, 4, 5]
    windows = list(sliding_window(data, 3))
    assert windows == [(1, 2, 3), (2, 3, 4), (3, 4, 5)]


def test_sliding_window_small_data():
    data = [1, 2]
    windows = list(sliding_window(data, 3))
    assert windows == []


def test_sliding_window_window_size_1():
    data = [10, 20, 30]
    windows = list(sliding_window(data, 1))
    assert windows == [(10,), (20,), (30,)]


# ==================== streaming_mean ====================

def test_streaming_mean():
    data = [1, 2, 3, 4, 5]
    means = list(streaming_mean(data))
    assert pytest.approx(means) == [1.0, 1.5, 2.0, 2.5, 3.0]


# ==================== streaming_variance ====================

def test_streaming_variance_ddof0():
    data = [1, 2, 3, 4, 5]
    variances = list(streaming_variance(data, ddof=0))
    assert len(variances) == 5
    # Последнее значение должно быть дисперсией выборки
    assert pytest.approx(variances[-1]) == 2.0


# ==================== streaming_pearson ====================

def test_streaming_pearson():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    corrs = list(streaming_pearson(x, y))
    assert len(corrs) == 5
    assert pytest.approx(corrs[-1]) == 1.0


# ==================== read_numbers_from_file ====================

def test_read_numbers_from_file(tmp_path):
    file = tmp_path / "numbers.txt"
    file.write_text("1 2 3\n4,5\n6 7 8\n")

    numbers = list(read_numbers_from_file(str(file)))
    assert numbers == [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]