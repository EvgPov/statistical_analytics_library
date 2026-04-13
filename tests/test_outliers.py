import pytest
from src.my_stats_lib.outliers import detect_outliers_iqr, remove_outliers
from src.my_stats_lib.exceptions import StatisticError

def test_detect_outliers_iqr_basic():
    data = [1, 2, 3, 4, 5, 6, 7, 100, 200]
    outliers = detect_outliers_iqr(data)
    assert outliers == [7, 8]  # индексы 100 и 200


def test_detect_outliers_iqr_no_outliers():
    data = [10, 12, 11, 13, 14, 12, 11]
    outliers = detect_outliers_iqr(data)
    assert outliers == []


def test_detect_outliers_iqr_small_data_raises():
    with pytest.raises(StatisticError):
        detect_outliers_iqr([1, 2, 3])  # меньше 4 элементов


def test_detect_outliers_iqr_custom_k():
    data = [1, 2, 3, 4, 5, 6, 7, 50]
    outliers = detect_outliers_iqr(data, k=2.0)
    assert outliers == [7]

def test_remove_outliers_iqr():
    data = [1, 2, 3, 4, 5, 6, 7, 100, 200]
    cleaned = list(remove_outliers(data))
    assert cleaned == [1, 2, 3, 4, 5, 6, 7]


def test_remove_outliers_no_outliers():
    data = [10, 11, 12, 13, 14]
    cleaned = list(remove_outliers(data))
    assert cleaned == data


def test_remove_outliers_generator_input():
    data = (x for x in [1, 2, 3, 100, 4, 5])
    cleaned = list(remove_outliers(data))
    assert cleaned == [1, 2, 3, 4, 5]


def test_remove_outliers_unsupported_method():
    with pytest.raises(ValueError):
        list(remove_outliers([1, 2, 3], method='zscore'))