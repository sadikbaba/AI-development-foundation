#  my own way to understand it
# expected value = Σ (value × probability)


def expected_value(values, probabilities):

    if len(values) != len(probabilities):
        return

    total_prob = 0
    for i in range(len(probabilities)):
        total_prob += probabilities[i]
    if total_prob != 1:
        return

    # value can be anything they have eg students. 3 students has 3 values [30, 40, 50]
    # probability can be anything they have eg students. 3 students has 3 probabilities [0.1, 0.4, 0.5]

    # to get the expected value you will do this
    expected_value = 0
    for i in range(len(values)):
        # values[i] is the value of the student
        value = values[i]
        # probabilities[i] is the probability of  this value/outcome
        probability = probabilities[i]
        expected_value += value * probability
    return expected_value


values = [5, 10, 15]
probabilities = [0.1, 0.4, 0.5]

print(expected_value(values, probabilities))

values = [0, 20, 50]
probabilities = [0.5, 0.3, 0.2]

print(expected_value(values, probabilities))
