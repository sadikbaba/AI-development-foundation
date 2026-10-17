# r = sum of (value_x - mean_x) (value_y - mean_y) / sqrt(sum of (value_x - mean_x)^2 * sum of (value_y - mean_y)^2)
import math


def mean_number(values):
    return sum(values) / len(values)


def correlation(values_x, values_y):
    mean_x = mean_number(values_x)
    mean_y = mean_number(values_y)

    numerator = 0
    sum_dx_squared = 0
    sum_dy_squared = 0

    for i in range(len(values_x)):
        dx = values_x[i] - mean_x
        dy = values_y[i] - mean_y

        numerator += dx * dy
        sum_dx_squared += dx**2
        sum_dy_squared += dy**2

    denominator = math.sqrt(sum_dx_squared * sum_dy_squared)

    r = numerator / denominator
    return r


if __name__ == "__main__":
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]

    print(correlation(x, y))

    x = [1, 2, 3]
    y = [6, 4, 2]
    print(correlation(x, y))

    x = [10, 20, 30, 40, 50]
    y = [20, 40, 60, 80, 100]
    print(correlation(x, y))
