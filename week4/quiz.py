import numpy as np

A = np.array([
    [-1, 3],
    [2, -4]
])

B = np.array([
    [0, 2],
    [2, -4]
])

D = [
    [-1, 5],
    [4, -8]
]

C = B @ A
print(C)
print(C[0][1])