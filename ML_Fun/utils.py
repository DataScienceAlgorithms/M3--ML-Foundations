
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

def get_column(table, header, col_name):
    col_index = header.index(col_name)
    col = []
    for row in table:
        col.append(row[col_index])

    return col


def group_by(table, header, group_by_col_name):
    group_by_col_index = header.index(group_by_col_name)
    groups = {}

    for row in table:
        group_by_val = row[group_by_col_index]

        if group_by_val not in groups:
            groups[group_by_val] = []

        groups[group_by_val].append(row)

    return list(groups.keys()), list(groups.values())