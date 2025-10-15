import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc

def sqrt_iterate(y0, x, tol=1e-6):
    y0 = y0
    while abs(x - y0**2) > tol:
        y0 = 0.5 * (y0 + x / y0)
    return y0

y = sqrt_iterate(12, 9)

print(y)

# A = np.array([
#     [1, 2, 3],
#     [3, 3, 3],
#     [4, 5, 1],
# ])

# B = np.array([
#     [2, 2, 2],
#     [5, 4, 3],
#     [2, 2, 23],
# ])

# a = A*B
# b = B*A

# print(a)
# print(B)