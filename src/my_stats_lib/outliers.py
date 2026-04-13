from .utils import ensure_list
from .exceptions import StatisticError

def detect_outliers_iqr(data, k=1.5):
    data_list = ensure_list(data)

    if len(data_list) < 4:
        raise StatisticError("Недостаточно данных для вычисления квартилей (минимум 4 элемента)")

    sorted_data = sorted(data_list)
    n = len(sorted_data)

    q1 = sorted_data[n // 4]
    q3 = sorted_data[3 * n // 4]
    iqr = q3 - q1

    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr

    outliers = [i for i, val in enumerate(data_list)
                if val < lower_bound or val > upper_bound]

    return outliers

def remove_outliers(data, method='iqr', **kwargs):
    if method != 'iqr':
        raise ValueError(f"Метод '{method}' не поддерживается. Используйте 'iqr'.")
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        data_list = ensure_list(data)

    outlier_indices = set(detect_outliers_iqr(data_list, **kwargs))

    for i, value in enumerate(data_list):
        if i not in outlier_indices:
            yield value