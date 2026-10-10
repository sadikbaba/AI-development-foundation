s = {1, 2, 3, 4, 5, 6}


def probability(s):
    A = set()
    for i in s:
        if i > 4:
            A.add(i)

    # math the formula
    # probability P(A) = possible outcomes / total outcomes
    len_A = len(A)
    len_s = len(s)

    ans = (len_A / len_s) * 100  # 100 means 100 percent

    return f"{round(ans, 2)}%"


prob = probability(s)
print(prob)


# probability distribution

s = {1, 2, 3, 4, 5, 6}

## For a fair die:
# P(x) = 1 / total number of possible outcomes
# x represents one possible outcome


def probability_distribution(s):
    # set of all possible outcomes
    # math the formula
    len_s = len(s)
    ans = 1 / len_s
    dist = {}
    for i in s:
        dist[i] = round(ans, 4)
    return dist


prob_dist = probability_distribution(s)
print(prob_dist)
