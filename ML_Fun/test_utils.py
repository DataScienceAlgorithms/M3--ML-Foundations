import numpy as np
from scipy import stats
import statistics
import utils

def test_mean():
    numbers = [10, 20, 30]
    expected = 20  # Desk calculation
    actual = utils.calculate_mean(numbers)
    assert actual == expected

def test_mean_known():
    numbers= [50, 20, 70, 30]
    expected = statistics.mean(numbers)  #known implementation
    actual = utils.calculate_mean(numbers)
    assert actual == expected

def test_compute_slope_intercept():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    expected = stats.linregress(x, y)

    m, b = utils.compute_slope_intercept(x, y)

    assert np.isclose(m, expected.slope)
    assert np.isclose(b, expected.intercept)
    print(m,b)

