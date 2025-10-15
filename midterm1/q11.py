import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sc

R1 = R2 = R3 = 1.0
R4 = R5 = 2.0

Vs = 15.0

A = np.array([
    [R2+R4, -R2, -R4],
    [-R2, R1+R2+R3, -R3],
    [-R4, -R3, R3+R4+R5],
])

b = np.array([15.0, 0.0, 0.0])

x = np.linalg.solve(A, b)

print(x)