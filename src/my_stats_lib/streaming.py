# src/my_stats_lib/streaming.py
import math
from collections import deque


def read_numbers_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            for token in line.replace(',', ' ').replace('\t', ' ').split():
                try:
                    yield float(token)
                except ValueError:
                    pass


def sliding_window(iterable, window_size):
    if window_size < 1:
        return
    it = iter(iterable)
    window = deque(maxlen=window_size)
    for item in it:
        window.append(item)
        if len(window) == window_size:
            yield tuple(window)


def streaming_mean(iterable):
    total = 0.0
    count = 0
    for x in iterable:
        total += x
        count += 1
        yield total / count


def streaming_variance(iterable, ddof=0):
    count = 0
    mean_val = 0.0
    m2 = 0.0
    for x in iterable:
        count += 1
        delta = x - mean_val
        mean_val += delta / count
        delta2 = x - mean_val
        m2 += delta * delta2

        if count > ddof:
            yield m2 / (count - ddof)
        else:
            yield 0.0


def streaming_pearson(x_iter, y_iter):
    """Онлайн-коэффициент корреляции Пирсона."""
    n = 0
    sum_x = sum_y = sum_xy = sum_x2 = sum_y2 = 0.0

    for x, y in zip(x_iter, y_iter):
        n += 1
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x2 += x * x
        sum_y2 += y * y

        if n < 2:
            yield 0.0
            continue

        numerator = n * sum_xy - sum_x * sum_y
        denom_x = n * sum_x2 - sum_x ** 2
        denom_y = n * sum_y2 - sum_y ** 2

        if denom_x <= 0 or denom_y <= 0:
            yield 0.0
        else:
            yield numerator / math.sqrt(denom_x * denom_y)