# Variance = sum of (each value - mean)² / number of values
## variance = Σ(value - mean)² / number_of_values


def mean_number(values):
    return sum(values) / len(values)

def variance(values):
    mean = mean_number(values)

    variance = 0
    for value in values:
        variance += (value - mean) ** 2

    ans = variance / len(values)
    return ans


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    print(variance(values))

    values = [2,2,8]
    print(variance(values))

    values = [4, 4, 4]
    print(variance(values))

    values = [1, 4, 7]
    print(variance(values))