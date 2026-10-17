# For every point on x, y also gain point

# slope = (y2 - y1) / (x2 - x1)
def calculate_slope(a, b):

    #  slope

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    if x1 == x2 :
        return None

    slope = (y2 - y1) / (x2 - x1)

    return slope


a = [1,4 ]
b = [3, 10]


if __name__ == "__main__":
    print("\nSlope")
    print(calculate_slope(a, b))

    a = [2, 4]
    b = [2, 10]
    print(calculate_slope(a, b))



# Derivative formula:
# f'(x) = lim(h -> 0) [f(x + h) - f(x)] / h
#
# Meaning:
# h = small change in x
# f(x + h) = new output after x changes by h
# f(x) = current output
# f(x + h) - f(x) = change in y
# divide by h = change in y / change in x
# lim(h -> 0) = make h smaller and smaller and see what value the slope approaches


# Example:
# f(x) = x^2
# x = 2
#
# f'(2) = lim(h -> 0) [f(2 + h) - f(2)] / h
#
# Using h = 0.1:
# f(2) = 4
# f(2.1) = 4.41
#
# slope = (4.41 - 4) / 0.1
# slope = 4.1
#
# Using h = 0.01:
# slope = 4.01
#
# As h gets closer to 0:
# slope gets closer to 4
#
# Therefore:
# f'(2) = 4

def calculate_derivative(x, h):

    if h == 0:
        return None

    right_hand = (x +h) **2
    left_hand = x**2

    numerator = right_hand - left_hand
    denominator = h
    derivative = numerator / denominator

    return derivative


if __name__ == "__main__":
    print("\nDerivative")
    print(calculate_derivative(2, 0.1))
    print(calculate_derivative(2, 0.01))
    print(calculate_derivative(2, 0.001))
    print(calculate_derivative(2, 0.0001))

# Power rule:
# f(x) = x^n
# f'(x) = n * x^(n - 1)
#
# Steps:
# 1. Take the exponent n
# 2. Put it in front
# 3. Subtract 1 from the exponent

# f(x) = x^3
# f'(x) = 3 * x^(3 - 1)
# f'(x) = 3 * x^2

def power_rule_derivative(x, n):
    return n * (x ** (n - 1))

if __name__ == "__main__":
    print("\nPower rule")
    print(power_rule_derivative(2, 3))



# Gradient formula:
#
# For a function with two inputs:
# f(x, y)
#
# gradient = [
#     partial derivative with respect to x,
#     partial derivative with respect to y
# ]
#
# Written mathematically:
# ∇f(x, y) = [∂f/∂x, ∂f/∂y]
#
# Example:
# f(x, y) = x^2 + y^2
#
# derivative with respect to x:
# ∂f/∂x = 2x
#
# derivative with respect to y:
# ∂f/∂y = 2y
#
# therefore:
# ∇f(x, y) = [2x, 2y]


# x = 1
# y = 4
#
# gradient = [2 * 1, 2 * 4]
# gradient = [2, 8]


def calculate_gradient(x, y, power=0):
    if power == 0:
        return [0, 0]

    gradient = []

    gradient.append(power * (x ** (power - 1)))
    gradient.append(power * (y ** (power - 1)))

    return gradient

if __name__ == "__main__":
    print("\nGradient")
    print(calculate_gradient(1, 4, 2))
    print(calculate_gradient(1, 4, 3))
    print(calculate_gradient(1, 4, 4))

    print(calculate_gradient(2, 4, 0))
    print(calculate_gradient(2, 4, 1))
    print(calculate_gradient(2, 4,))
