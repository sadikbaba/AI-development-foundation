# formula for symmetric and skewed distributions

# g1 = ((1 / n) * sum((value_x - mean_x) ** 3)) / (standard_deviation_x ** 3)


import matplotlib.pyplot as plt


def mean_number(values):
    return sum(values) / len(values)


def variance(values):
    mean = mean_number(values)

    variance = 0
    for value in values:
        variance += (value - mean) ** 2

    ans = variance / len(values)
    return ans


def standard_deviation(values):
    variance_value = variance(values)
    std = variance_value**0.5

    return std


def skewnessOrSymmetry(values):
    mean = mean_number(values)

    std = standard_deviation(values)

    sum_of_cubed_deviations = 0

    for value in values:
        sum_of_cubed_deviations += (value - mean) ** 3

    g1 = (sum_of_cubed_deviations / len(values)) / (std**3)
    return g1


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    print(skewnessOrSymmetry(values))

    values = [2, 2, 8]
    print(skewnessOrSymmetry(values))

    values = [1, 7, 7]
    print(skewnessOrSymmetry(values))


values = [1, 17, 18, 18, 19, 19, 20]

plt.hist(values)
plt.savefig("data/histogram.png")
