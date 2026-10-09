import numpy as np
from scipy import stats
import statistics
import utils

def test_mean():
    numbers = [10, 20, 30]
    expected = 20  # Desk calculation
    actual = utils.calculate_mean(numbers)
    assert np.isclose(actual,expected)
   

def test_mean_known():
    numbers= [50, 20, 70, 30]
    expected = statistics.mean(numbers)  #known implementation
    actual = utils.calculate_mean(numbers)
    assert np.isclose(actual, expected)

def test_compute_slope_intercept():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    expected = stats.linregress(x, y)

    m, b = utils.compute_slope_intercept(x, y)

    assert np.isclose(m, expected.slope)
    assert np.isclose(b, expected.intercept)
    print(m,b)



def test_group_by():
    header = ["Name", "Year"]
    table = [
        ["Alice", 2024],
        ["Bob", 2025],
        ["Charlie", 2024]
    ]

    expected_values = [2024, 2025]
    expected_subtables = [
        [["Alice", 2024], ["Charlie", 2024]],
        [["Bob", 2025]]
    ]

    actual_values, actual_subtables = utils.group_by(
        table, header, "Year"
    )

    assert actual_values == expected_values
    assert actual_subtables == expected_subtables