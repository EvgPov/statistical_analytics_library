from .core import mean, std
from .utils import ensure_list

def covariance(x, y, ddof=1):
    x_list = ensure_list(x)
    y_list = ensure_list(y)

    if len(x_list) != len(y_list):
        raise ValueError("x и y должны иметь одинаковую длину")
    if len(x_list) == 0:
        raise ValueError("Данные не могут быть пустыми")
    if len(x_list) <= ddof:
        raise ValueError(f"Недостаточно данных для ddof={ddof}")

    n = len(x_list)
    mx = mean(x_list)
    my = mean(y_list)

    cov_sum = sum((xi - mx) * (yi - my) for xi, yi in zip(x_list, y_list))

    return cov_sum / (n - ddof)


def pearson_correlation(x, y):
    x_list = ensure_list(x)
    y_list = ensure_list(y)

    if len(x_list) != len(y_list):
        raise ValueError("x и y должны иметь одинаковую длину")
    if len(x_list) < 2:
        raise ValueError("Для корреляции Пирсона нужно минимум 2 элемента")

    cov = covariance(x_list, y_list, ddof=0)
    sx = std(x_list, ddof=0)   # здесь нужна функция std из core
    sy = std(y_list, ddof=0)

    if sx == 0 or sy == 0:
        raise ValueError("Стандартное отклонение одной из выборок равно нулю")

    return cov / (sx * sy)