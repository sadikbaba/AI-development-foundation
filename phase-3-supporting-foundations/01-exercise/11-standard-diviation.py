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


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    print(standard_deviation(values))

    values = [2, 2, 8]
    print(standard_deviation(values))

    values = [4, 4, 4]
    print(standard_deviation(values))

    values = [1, 4, 7]
    print(standard_deviation(values))
