import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc

A = np.array([
    [0, 3, 0, 6],
    [1, 0, 2, 0],
    [0, 5, 5, 0],
    [0, 0, 7, 1],
])

b = np.array([18, -5, -25, -17], dtype=float)

x = np.linalg.solve(A, b)

print(x[1])

# c = A @ x

# print(c)