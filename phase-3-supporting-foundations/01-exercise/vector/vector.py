import numpy as np

vector = np.array([2, 3, 4])
vector2 = np.array([5, 1, 2])
scalar = 2


matrix_a = np.array([[1, 2], [3, 4]])

matrix_b = np.array([[5, 6], [7, 8]])

#  geometric meaning
a = np.array([1, 0])

same_direction = np.array([1, 0])
opposite_direction = np.array([-1, 0])
perpendicular = np.array([0, 1])


if __name__ == "__main__":
    print(vector)
    print(vector.shape)
    print("\n")
    print(matrix_a)
    print(matrix_a.shape)

    print("\n")
    print(vector + vector2)
    print(vector - vector2)
    print(scalar * vector)

    print("\n")

    result = np.dot(vector, vector2)
    print(result)

    print("\n")
    matrix_result = matrix_a @ matrix_b
    print(matrix_result)
    print(matrix_result.shape)

    print("\n")
    print(np.dot(a, same_direction))
    print(np.dot(a, opposite_direction))
    print(np.dot(a, perpendicular))

    a = np.array([2, 3])

    same_direction = np.array([4, 6])
    opposite_direction = np.array([-4, -6])
    perpendicular = np.array([3, -2])

    print("\n")
    print(np.dot(a, same_direction))
    print(np.dot(a, opposite_direction))
    print(np.dot(a, perpendicular))
