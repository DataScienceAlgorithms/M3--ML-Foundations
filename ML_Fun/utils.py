
def calculate_mean(numbers):
    """Return the arithmetic mean of a non-empty list of numbers."""
    return sum(numbers) / len(numbers)

def compute_slope_intercept(x, y):
    meanx = sum(x) / len(x)
    meany = sum(y) / len(y)

    num = sum([(x[i] - meanx) * (y[i] - meany) for i in range(len(x))])
    den = sum([(x[i] - meanx) ** 2 for i in range(len(x))])
    m = num / den
    # y = mx + b -> y - mx
    b = meany - m * meanx
    return m, b

def group_by(table, header, group_by_col_name):
    col = get_column(table, header, group_by_col_name)
    unique_col_values = sorted((set(col)))
    group_by_col_index = header.index(group_by_col_name)
    group_subtables = [[] for _ in unique_col_values]

    for row in table:
        group_by_val = row[group_by_col_index]
        subtable_index = unique_col_values.index(group_by_val)
        group_subtables[subtable_index].append(row)

    return unique_col_values, group_subtables