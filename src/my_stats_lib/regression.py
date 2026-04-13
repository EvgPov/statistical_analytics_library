from .core import mean
from .utils import ensure_list

from collections import namedtuple

RegressionModel = namedtuple(
    'RegressionModel',
    ['slope', 'intercept', 'r_squared', 'mse', 'predictions', 'residuals']
)


def linear_regression(x, y):
    """Простая линейная регрессия методом наименьших квадратов."""
    x_list = ensure_list(x)
    y_list = ensure_list(y)

    if len(x_list) != len(y_list):
        raise ValueError("x и y должны иметь одинаковую длину")
    if len(x_list) == 0:
        raise ValueError("Данные не могут быть пустыми")
    if len(x_list) < 2:
        raise ValueError("Для линейной регрессии нужно минимум 2 точки")

    n = len(x_list)
    mx = mean(x_list)
    my = mean(y_list)

    # Вычисляем slope (наклон)
    numerator = sum((xi - mx) * (yi - my) for xi, yi in zip(x_list, y_list))
    denominator = sum((xi - mx) ** 2 for xi in x_list)

    if denominator == 0:
        raise ValueError("Все значения x одинаковы — регрессия невозможна")

    slope = numerator / denominator
    intercept = my - slope * mx

    # Предсказанные значения
    predictions = [slope * xi + intercept for xi in x_list]

    # Остатки (residuals)
    residuals = [yi - pi for yi, pi in zip(y_list, predictions)]

    # Метрики качества
    ss_res = sum(r ** 2 for r in residuals)
    ss_tot = sum((yi - my) ** 2 for yi in y_list)
    r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0.0
    mse = ss_res / n

    return RegressionModel(
        slope=slope,
        intercept=intercept,
        r_squared=r_squared,
        mse=mse,
        predictions=predictions,
        residuals=residuals
    )


def predict(model, new_x):
    """Предсказание по модели линейной регрессии."""
    if not hasattr(model, 'slope') or not hasattr(model, 'intercept'):
        raise TypeError("Некорректная модель регрессии. Ожидается объект RegressionModel.")

    if isinstance(new_x, (int, float)):
        return model.slope * new_x + model.intercept

    # Если передан итератор/список — возвращаем генератор
    return (model.slope * xi + model.intercept for xi in new_x)