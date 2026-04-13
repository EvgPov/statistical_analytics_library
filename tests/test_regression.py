import pytest
from src.my_stats_lib.regression import linear_regression, predict
from src.my_stats_lib.exceptions import StatisticError

# linear_regression
def test_linear_regression_perfect():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    model = linear_regression(x, y)

    assert pytest.approx(model.slope) == 2.0
    assert pytest.approx(model.intercept) == 0.0
    assert pytest.approx(model.r_squared) == 1.0
    assert pytest.approx(model.mse) == 0.0


def test_linear_regression_real_data():
    x = [1, 2, 3, 4, 5]
    y = [3, 5, 7, 6, 9]
    model = linear_regression(x, y)

    assert pytest.approx(model.slope, abs=0.01) == 1.3
    assert pytest.approx(model.intercept, abs=0.01) == 2.1
    assert 0 < model.r_squared < 1
    assert model.mse > 0


def test_linear_regression_empty_raises():
    with pytest.raises(ValueError):
        linear_regression([], [])


def test_linear_regression_different_length_raises():
    with pytest.raises(ValueError):
        linear_regression([1, 2, 3], [1, 2])


def test_linear_regression_constant_x_raises():
    with pytest.raises(ValueError):
        linear_regression([2, 2, 2, 2], [1, 3, 5, 7])


def test_predict_single_value():
    x = [1, 2, 3]
    y = [2, 4, 6]
    model = linear_regression(x, y)
    assert pytest.approx(predict(model, 4)) == 8.0


def test_predict_list():
    x = [1, 2, 3]
    y = [2, 4, 6]
    model = linear_regression(x, y)
    predictions = list(predict(model, [4, 5, 6]))
    assert pytest.approx(predictions) == [8.0, 10.0, 12.0]

def test_linear_regression_returns_namedtuple_like():
    x = [1, 2, 3]
    y = [3, 5, 7]
    model = linear_regression(x, y)

    assert hasattr(model, 'slope')
    assert hasattr(model, 'intercept')
    assert hasattr(model, 'r_squared')
    assert hasattr(model, 'mse')
    assert hasattr(model, 'predictions')
    assert hasattr(model, 'residuals')