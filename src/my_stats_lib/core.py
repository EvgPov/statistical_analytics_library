import math
from collections import Counter
from .exceptions import StatisticError
from .utils import ensure_list


def mean(data):
    total = 0.0
    count = 0
    for x in data:
        total += x
        count += 1
    if count == 0:
        raise StatisticError("Данные пусты")
    return total / count


def median(data):
    data_list = ensure_list(data)
    if not data_list:
        raise StatisticError("Данные пусты")
    sorted_data = sorted(data_list)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_data[mid])
    return (sorted_data[mid - 1] + sorted_data[mid]) / 2


def mode(data):
    data_list = ensure_list(data)
    if not data_list:
        raise StatisticError("Данные пусты")
    counter = Counter(data_list)
    max_count = max(counter.values())
    # Возвращаем первую встретившуюся моду
    for value in data_list:
        if counter[value] == max_count:
            return float(value)


def variance(data, ddof=0):
    data_list = ensure_list(data)
    n = len(data_list)
    if n == 0 or ddof >= n:
        raise StatisticError("Данные пусты или ddof слишком большой")
    m = mean(data_list)
    return sum((x - m) ** 2 for x in data_list) / (n - ddof)


def std(data, ddof=0):
    return math.sqrt(variance(data, ddof))