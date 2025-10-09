import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])

b = np.array([8, 3, 5])

C = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
])

answerA = A + C.T
answerB = 2 * A
answerC = A @ b
answerD = b.T @ A.T
answerE = A @ A.T

# print("answer A: ", answerA)
# print("answer B: ", answerB)
# print("answer C: ", answerC)
# print("answer D: ", answerD)
# print("answer E: ", answerE)
